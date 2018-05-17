# We reuse a fraction of code in http://bitbucket.org/omerlevy/hyperwords.
# Using the numpy and similarity matrix largely speed up the evaluation process,
# compared with evaluation scripts in word2vec and GloVe

import numpy as np
import argparse
import random
from scipy.sparse import dok_matrix, csr_matrix


def load_matrix(f_path):
    with open(f_path, errors='ignore') as f:
        row, col, data, iw = [], [], [], []
        first_line = True
        lines_num = 0
        for line in f:
            if first_line:
                first_line = False
                words_num = int(line.rstrip().split()[0])
                dim = int(line.rstrip().split()[1])
                continue
            line = line.rstrip().split(' ')
            word = line[0]
            iw.append(word)
            vector = line[1:]
            for v in vector:
                row.append(lines_num)
                col.append(int(v.split(":")[0]))
                data.append(float(v.split(":")[1]))
            lines_num += 1
        wi = {}
        for i in range(len(iw)):
            wi[iw[i]] = i
        row = np.array(row)
        col = np.array(col)
        data = np.array(data)
        matrix = csr_matrix((data, (row, col)), shape=(words_num, dim))
        return matrix, iw, wi


def load_vocabulary(path):
    with open(path) as f:
        vocab = [line.strip().split()[0] for line in f if len(line) > 0]
    return dict([(a, i) for i, a in enumerate(vocab)]), vocab


def read_analogy(path, iw):
    analogy = {}
    analogy_type = ""
    with open(path) as f:
        for line in f:
            oov = 0
            if line.strip().split()[0] == ':':
                analogy_type = line.strip().split()[1]
                analogy[analogy_type] = {}
                analogy[analogy_type]["questions"] = []
                analogy[analogy_type]["total"] = 0
                analogy[analogy_type]["seen"] = 0
                continue
            analogy_question = line.strip().split()
            for w in analogy_question[:3]:
                if w not in iw:
                    oov = 1
            if oov == 1:
                analogy[analogy_type]["total"] += 1
                continue
            analogy[analogy_type]["total"] += 1
            analogy[analogy_type]["seen"] += 1
            analogy[analogy_type]["questions"].append(analogy_question)

        for t in analogy:
            analogy[t]['iw'] = []
            analogy[t]['wi'] = {}
            for question in analogy[t]["questions"]:
                for w in question:
                    if w not in analogy[t]['iw']:
                        analogy[t]['iw'].append(w)
            for i, w in enumerate(analogy[t]['iw']):
                analogy[t]['wi'][w] = i
        return analogy


def normalize(matrix):
    matrix2 = matrix.copy()
    matrix2.data **= 2
    norm = np.reciprocal(np.sqrt(np.array(matrix2.sum(axis=1))[:, 0]))
    normalizer = dok_matrix((len(norm), len(norm)))
    normalizer.setdiag(norm)
    matrix = normalizer.tocsr().dot(matrix)
    return matrix


def guess(sims, analogy, analogy_type, iw, wi, word_a, word_b, word_c):
    sim_a = sims[analogy[analogy_type]["wi"][word_a]]
    sim_b = sims[analogy[analogy_type]["wi"][word_b]]
    sim_c = sims[analogy[analogy_type]["wi"][word_c]]

    add_sim = -sim_a+sim_b+sim_c
    add_sim[wi[word_a]] = 0
    add_sim[wi[word_b]] = 0
    add_sim[wi[word_c]] = 0
    guess_add = iw[np.nanargmax(add_sim)]

    mul_sim = sim_b * sim_c * np.reciprocal(sim_a+0.01)
    mul_sim[wi[word_a]] = 0
    mul_sim[wi[word_b]] = 0
    mul_sim[wi[word_c]] = 0
    guess_mul = iw[np.nanargmax(mul_sim)]
    return guess_add, guess_mul


def main():
    neg = 1
    vectors_path = "embedding_sample/sparse_small.txt"
    analogy_path = "CA8/morphological.txt"
    results = {}

    myParser = argparse.ArgumentParser()
    myParser.add_argument('-v', '--vectors', type=str, help="Vectors path")
    myParser.add_argument('-a', '--analogy', type=str, help="Analogy benchmark path")
    args = myParser.parse_args()
    if args.vectors:
        vectors_path = args.vectors
    if args.analogy:
        analogy_path = args.analogy

    matrix, iw, wi = load_matrix(vectors_path)  # Read matrix into the memory
    matrix = normalize(matrix)
    analogy = read_analogy(analogy_path, iw)
    for analogy_type in analogy.keys():  # Calculate the accuracy for each relation type
        correct_add_num, correct_mul_num = 0, 0
        analogy_matrix = matrix[[wi[w] if w in wi else random.randint(0, len(wi)-1) for w in analogy[analogy_type]["iw"]]]
        sims = analogy_matrix.dot(matrix.T)
        sims = np.array(sims.todense())
        for question in analogy[analogy_type]["questions"]:  # Loop for each analogy question
            word_a, word_b, word_c, word_d = question
            guess_add, guess_mul = guess(sims, analogy, analogy_type, iw, wi, word_a, word_b, word_c)
            if guess_add == word_d:
                correct_add_num += 1
            if guess_mul == word_d:
                correct_mul_num += 1
        cov = float(analogy[analogy_type]["seen"]) / analogy[analogy_type]["total"]
        if analogy[analogy_type]["seen"] == 0:
            acc_add = 0
            acc_mul = 0
            print (analogy_type + " add/mul: " + str(round(0.0, 3)) + "/" + str(round(0.0, 3)))
        else:
            acc_add = float(correct_add_num) / analogy[analogy_type]["seen"]
            acc_mul = float(correct_mul_num) / analogy[analogy_type]["seen"]
            print (analogy_type + " add/mul: " + str(round(acc_add, 3)) + "/" + str(round(acc_mul, 3)))
        # Store the results
        results[analogy_type] = {}
        results[analogy_type]["coverage"] = [cov, analogy[analogy_type]["seen"], analogy[analogy_type]["total"]]
        results[analogy_type]["accuracy_add"] = [acc_add, correct_add_num, analogy[analogy_type]["seen"]]
        results[analogy_type]["accuracy_mul"] = [acc_mul, correct_mul_num, analogy[analogy_type]["seen"]]

    correct_add_num, correct_mul_num, seen = 0, 0, 0
    for analogy_type in results:
        correct_add_num += results[analogy_type]["accuracy_add"][1]
        correct_mul_num += results[analogy_type]["accuracy_mul"][1]
        seen += results[analogy_type]["coverage"][1]

    # print results
    print("Total accuracy (add): " + str(round(float(correct_add_num)/seen, 3)))
    print("Total accuracy (mul): " + str(round(float(correct_mul_num)/seen, 3)))


if __name__ == '__main__':
    main()
