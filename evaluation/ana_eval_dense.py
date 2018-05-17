# We reuse a fraction of code in http://bitbucket.org/omerlevy/hyperwords.
# Using the numpy and similarity matrix largely speed up the evaluation process,
# compared with evaluation scripts in word2vec and GloVe

import numpy as np
import argparse
import random


def read_vectors(path, topn):  # read top n word vectors, i.e. top is 10000
    lines_num, dim = 0, 0
    vectors = {}
    iw = []
    wi = {}
    with open(path, encoding='utf-8', errors='ignore') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                dim = int(line.rstrip().split()[1])
                continue
            lines_num += 1
            tokens = line.rstrip().split(' ')
            vectors[tokens[0]] = np.asarray([float(x) for x in tokens[1:]])
            iw.append(tokens[0])
            if topn != 0 and lines_num >= topn:
                break
    for i, w in enumerate(iw):
        wi[w] = i
    return vectors, iw, wi, dim


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
    norm = np.sqrt(np.sum(matrix * matrix, axis=1))
    matrix = matrix / norm[:, np.newaxis]
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
    vectors_path = "embedding_sample/dense_small.txt"
    analogy_path = "CA8/morphological.txt"
    topn = 0
    results = {}  # Records the results
    myParser = argparse.ArgumentParser()
    myParser.add_argument('-v', '--vectors', type=str, help="Vectors path")
    myParser.add_argument('-a', '--analogy', type=str, help="Analogy benchmark path")
    myParser.add_argument('-t', '--topn', type=int, help="Read top n word vectors")
    args = myParser.parse_args()
    if args.vectors:
        vectors_path = args.vectors
    if args.analogy:
        analogy_path = args.analogy
    if args.topn:
        topn = args.topn

    vectors, iw, wi, dim = read_vectors(vectors_path, topn)  # Read top n word vectors. Read all vectors when topn is 0
    analogy = read_analogy(analogy_path, iw)  # Read analogy questions

    # Turn vectors into numpy format and normalize them
    matrix = np.zeros(shape=(len(iw), dim), dtype=np.float32)
    for i, word in enumerate(iw):
        matrix[i, :] = vectors[word]
    matrix = normalize(matrix)

    for analogy_type in analogy.keys():  # Calculate the accuracy for each relation type
        correct_add_num, correct_mul_num = 0, 0
        analogy_matrix = matrix[[wi[w] if w in wi else random.randint(0, len(wi)-1) for w in analogy[analogy_type]["iw"]]]
        sims = analogy_matrix.dot(matrix.T)
        sims = (sims + 1)/2  # Transform similarity scores to positive numbers (for mul evaluation)
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
            print(analogy_type + " add/mul: " + str(round(0.0, 3)) + "/" + str(round(0.0, 3)))
        else:
            acc_add = float(correct_add_num) / analogy[analogy_type]["seen"]
            acc_mul = float(correct_mul_num) / analogy[analogy_type]["seen"]
            print(analogy_type + " add/mul: " + str(round(acc_add, 3)) + "/" + str(round(acc_mul, 3)))
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
    if seen == 0:
        print("Total accuracy (add): " + str(round(0.0, 3)))
        print("Total accuracy (mul): " + str(round(0.0, 3)))
    else:
        print("Total accuracy (add): " + str(round(float(correct_add_num)/seen, 3)))
        print("Total accuracy (mul): " + str(round(float(correct_mul_num)/seen, 3)))


if __name__ == '__main__':
    main()
