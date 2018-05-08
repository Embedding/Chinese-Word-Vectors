# Chinese Word Vectors 中文词向量
This project provides Chinese Word Vectors (embeddings) trained with different **representations** (dense and sparse), **context features** (word, ngram, character, and more), and **corpora**. One can easily obtain pre-trained vectors with different properties and use them for downstream tasks. 

Moreover, we provide a Chinese analogical reasoning dataset **CA8** and an evaluation toolkit for users to evaluate the quality of their word vectors.

## Format
The pre-trained vector files are in text format. Each line contains a word and its vector. Each value is separated by space. The first line records the meta information: the first number indicates the number of words in the file and the second indicates the dimension size. 

Besides dense word vectors (trained with SGNS), we also provide sparse vectors (trained with PPMI). They are in the same format with liblinear, where the number before " : " denotes dimension index and the number after the " : " denotes the value. 

## Pre-trained Chinese Word Vectors

### Basic Settings

<table>
  <tr align="center">
    <td><b>Window Size</b></td>
    <td><b>Dynamic Window</b></td>
    <td><b>Sub-sampling</b></td>
    <td><b>Low-Frequency Word</b></td>
  </tr>
  <tr align="center">
    <td>5</td>
    <td>Yes</td>
    <td>1e-5</td>
    <td>10</td>
  </tr>
</table>

### Various Domains

Chinese Word Vectors trained with different representations, context features, and corpora.

<table align="center">
    <tr align="center">
        <td></td>
        <td colspan="4"><b>Word2ec / Skip-Gram with Negative Sampling (SGNS)</b></td>
    </tr>
    <tr  align="center">
      <td>Corpus</td>
      <td>Word</td>
      <td>Word + Ngram</td>
      <td>Word + Character</td>
      <td>Word + Character + Ngram</td>
    </tr>
    <tr  align="center">
      <td>Baidu Encyclopedia 百度百科</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书</td>
      <td colspan="4"><a href="http://www.baidu.com">300d</a><sup>*</sup></td>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
</table>

<table align="center">
    <tr align="center">
        <td></td>
        <td colspan="4"><b>Positive Pointwise Mutual Information (PPMI)</b></td>
    </tr>
    <tr  align="center">
      <td>Corpus</td>
      <td>Word</td>
      <td>Word + Ngram</td>
      <td>Word + Character</td>
      <td>Word + Character + Ngram</td>
    </tr>
    <tr  align="center">
      <td>Baidu Encyclopedia 百度百科</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书</td>
      <td colspan="4"><a href="http://www.baidu.com">300d</a><sup>*</sup></td>
    </tr>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合</td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
      <td><a href="http://www.baidu.com">300d</a></td>
    </tr>
</table>

<sup>\*</sup>Character embeddings are provided, since most of Hanzi are word in the archaic Chinese.

### Various Co-occurrence Information

We release word vectors upon different co-occurrence statistics. Target and context vectors are often called input and output vectors in some related papers. 

In this part, one can obtain vectors of arbitrary linguistic units beyond word. For example, character vectors is in the context vectors of word-character.

All vectors are trained by SGNS on Baidu Encyclopedia.

<table>
  <tr align="center">
    <td><b>Feature</b></td>
    <td><b>Co-occurrence Type</b></td>
    <td><b>Target Word Vectors</b></td>
    <td><b>Context Word Vectors</b></td>
  </tr>
  
  <tr align="center">
  	<td rowspan="1">Word</td>
    <td>Word → Word</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>

  <tr align="center">
    <td rowspan="3">Ngram</td>
    <td>Word → Ngram (1-2)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Ngram (1-3)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Ngram (1-2) → Ngram (1-2)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  
  <tr align="center">
    <td rowspan="3">Character</td>
    <td>Word → Character (1)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-2)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-4)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  
  <tr align="center">
  	<td rowspan="1">Radical</td>
    <td>Radical</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  
  <tr align="center">
    <td rowspan="2">Position</td>
    <td>Word → Word (left/right)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Word (distance)</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  
  <tr align="center">
    <td>Global</td>
    <td>Word → Text</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
    
  <tr align="center">
    <td rowspan="2">Syntactic Feature</td>
    <td>Word → POS</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Dependency</td>
    <td><a href="http://www.baidu.com">300d</a></td>
 	<td><a href="http://www.baidu.com">300d</a></td>
  </tr>
</table>

## Representations
Existing word representation methods fall into one of the two classes, **dense** and **sparse** represnetations. SGNS model (a model in word2vec toolkit) and PPMI model are respectively typical methods of these two classes. SGNS model trains low-dimensional real (dense) vectors through a shallow neural network. It is also called neural embedding method. PPMI model is a sparse bag-of-feature representation weighted by positive-pointwise-mutual-information (PPMI) weighting scheme.

## Context Features
Three context features: **word**, **ngram**, and **character** are commonly used in the word embedding literature. Most word representation methods essentially exploit word-word co-occurrence statistics, namely using word as context feature **(word feature)**. Inspired by language modeling problem, we introduce ngram feature into the context. Both word-word and word-ngram co-occurrence statistics are used for training **(ngram feature)**. For Chinese, characters (Hanzi) often convey strong semantics. To this end, we consider using word-word and word-character co-occurrence statistics for learning word vectors. The length of character-level ngrams ranges from 1 to 4 **(character feature)**.

Besides word, ngram, and character, there are other features which have substantial influence on properties of word vectors. For example, using entire text as context feature could introduce more topic information into word vectors; using dependency parse as context feature could add syntactic constraint to word vectors. 17 co-occurrence types are considered in this project.

## Corpus
We made great efforts to collect corpus across various domains. All text data are preprocessed by removing html and xml tags. Only the plain text are kept and [HanLP(v_1.5.3)](https://github.com/hankcs/HanLP) is used for word segmentation. The detailed corpora information is listed as follows:

<table>
	<tr align="center">
		<td><b>Corpus</b></td>
		<td><b>Size</b></td>
		<td><b>Tokens</b></td>
		<td><b>Vocabulary Size</b></td>
		<td><b>Description</b></td>
	</tr>
	<tr align="center">
		<td>Baidu Encyclopedia<br />百度百科</td>
		<td>4.3G</td>
		<td>745M</td>
		<td>271K</td>
		<td>Chinese Encyclopedia data from<br />https://baike.baidu.com/</td>
	</tr>
	<tr align="center">
		<td>Wikipedia_zh<br />中文维基百科</td>
		<td>1.2G</td>
		<td>223M</td>
		<td>133K</td>
		<td>Chinese Wikipedia data from<br />https://dumps.wikimedia.org/</td>
	</tr>
	<tr align="center">
		<td>People's Daily News<br />人民日报</td>
		<td>4.2G</td>
		<td>669M</td>
		<td>171K</td>
		<td>News data from People's Daily(1946-2017)<br />http://data.people.com.cn/</td>
	</tr>
	<tr align="center">
		<td>Sogou News<br />搜狗新闻</td>
		<td>4.0G</td>
		<td>657M</td>
		<td>176K</td>
		<td>News data provided by Sogou labs<br />http://www.sogou.com/labs/</td>
	</tr>
	<tr align="center">
		<td>Zhihu_QA<br />知乎问答</td>
		<td>2.2G</td>
		<td>384M</td>
		<td>123K</td>
		<td>Chinese QA data from<br />https://www.zhihu.com/</td>
	</tr>
	<tr align="center">
		<td>Weibo<br />微博</td>
		<td></td>
		<td></td>
		<td></td>
		<td>China-based microblogs from<br />https://weibo.com/</td>
	</tr>
	<tr align="center">
		<td>Literature<br />文学作品</td>
		<td></td>
		<td></td>
		<td></td>
		<td>8599 modern Chinese literature works</td>
	</tr>
	<tr align="center">
		<td>Complete Library in Four Sections<br />四库全书</td>
		<td></td>
		<td></td>
		<td></td>
		<td>It was the largest collection of texts in pre-modern China.</td>
	</tr>
	<tr align="center">
		<td>Mixed-large<br />综合</td>
		<td></td>
		<td></td>
		<td></td>
		<td>We build the large corpus by merging the above corpora.</td>
	</tr>
</table>

## Toolkits
All word vectors are trained by [ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit. Ngram2vec toolkit is a superset of [word2vec](https://github.com/svn2github/word2vec) and [fasttext](https://github.com/facebookresearch/fastText) toolkit, where arbitrary context features and models are supported.

## Chinese Word Analogy Benchmarks
The quality of word vectors is often evaluated by analogy question tasks. In this project, two benchmarks are exploited for evaluation. The first is CA-translated, where most analogy questions are directly translated from English benchmark. Although CA-translated has been widely used in many Chinese word embedding papers, it only contains questions of three semantic questions and covers 134 Chinese words. In contrast, CA8 is specifically designed for Chinese language. It contains 17813 analogy questions and covers comprehensive morphological and semantic relations. The CA-translated, CA8, and their detailed descriptions are provided in [**testsets**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets) folder.


## Evaluation Toolkit
We present an evaluation toolkit in [**evaluation**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/evaluation) folder. 

Run the following codes to evaluate your trained dense vectors.
```
$ python ana_eval_dense.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_dense.py -v <vector.txt> -a CA8/semantic.txt
```
Run the following codes to evaluate your sparse vectors.
```
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/semantic.txt
```

## Reference
Please cite the paper, if using these embeddings and CA8 dataset.

Shen Li, Zhe Zhao, Renfen Hu, Wensi Li, Tao Liu, Xiaoyong Du, <em>Analogical Reasoning on Chinese Morphological and Semantic Relations</em>, ACL 2018.

```
@InProceedings{shen2018analogical,
  title={Analogical Reasoning on Chinese Morphological and Semantic Relations},
  author={Shen, Li and Zhe, Zhao and Renfen, Hu and Wensi, Li and Tao, Liu and Xiaoyong, Du},
  year={2018},
}
```
