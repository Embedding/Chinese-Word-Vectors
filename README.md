# Chinese Word Vectors 中文词向量
This project provides 100+ Chinese Word Vectors (embeddings) trained with different **representations** (dense and sparse), **context features** (word, ngram, character, and more), and **corpora**. One can easily obtain pre-trained vectors with different properties and use them for downstream tasks. 

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
    <td><b>Iteration</b></td>
  </tr>
  <tr align="center">
    <td>5</td>
    <td>Yes</td>
    <td>1e-5</td>
    <td>10</td>
    <td>5</td>
  </tr>
</table>

### Various Domains

Chinese Word Vectors trained with different representations, context features, and corpora.

<table align="center">
    <tr align="center">
        <td colspan="5"><b>Word2vec / Skip-Gram with Negative Sampling (SGNS)</b></td>
    </tr>
    <tr align="center">
        <td rowspan="2">Corpus</td>
        <td colspan="4">Context Features</td>
    </tr>
    <tr  align="center">
      <td>Word</td>
      <td>Word + Ngram</td>
      <td>Word + Character</td>
      <td>Word + Character + Ngram</td>
    </tr>
    <tr  align="center">
      <td>Baidu Encyclopedia 百度百科</td>
      <td><a href="https://pan.baidu.com/s/1P_jpFuPI6K36PlmOLvdRJA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1C59ebYO14o1otnt3CK5cVA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1MsNSYjuglTROrojd9Ce2Xg">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="https://pan.baidu.com/s/1bqtoXFJTawJ-0d0-E_SXbQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1aQGcEX2GiIkplTKfwaA8Yw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1sgj5K1OjqSbIj02MJ3DSYw">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>People's Daily News 人民日报</td>
      <td><a href="https://pan.baidu.com/s/17er0CP00DUpH40lNsIKW1g">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1vdPSI6fOo9ALS6HNhNjezA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1JYVG5JJz-LkIQRh-Y2k77w">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="https://pan.baidu.com/s/1UyHTRF7LOqd3W9nehoS_xg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1niyJ2DtrAViSQA1VqdKcNA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1VJDR5r5pZ3mSzUeb454CMg">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td><a href="https://pan.baidu.com/s/1NNSBbS5YmudrleCrvL7BbA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1jKcDetB0GTORhd7qaNJ64A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1ov4YgJFHXRiYlvfNQgjFuA">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="https://pan.baidu.com/s/1wn3a3Vo5eA_Hxdbbxff-rw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1SnefWeGHQhw_yG14JYDZiw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1wDlK9oPVESvScmXqYtQvvw">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="https://pan.baidu.com/s/1ndWi40zwcRW8JJQzoO-1Mw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/158yIDYQUppWVM6H9YmM5iQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1XuMh5HnIsaf0q9CBLQqbaA">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书<sup>*</sup></td>
      <td>300d</td>
      <td>300d</td>
      <td>NAN</td>
      <td>NAN</td>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合</td>
      <td><a href="https://pan.baidu.com/s/108Wyhg0HEbVcpyDJ1RH4eQ">300d</a></td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
    </tr>
</table>

<table align="center">
    <tr align="center">
        <td colspan="5"><b>Positive Pointwise Mutual Information (PPMI)</b></td>
    </tr>
    <tr align="center">
        <td rowspan="2">Corpus</td>
        <td colspan="4">Context Features</td>
    </tr>
    <tr  align="center">
      <td>Word</td>
      <td>Word + Ngram</td>
      <td>Word + Character</td>
      <td>Word + Character + Ngram</td>
    </tr>
    <tr  align="center">
      <td>Baidu Encyclopedia 百度百科</td>
      <td>300d</td>
      <td>300d</td>
      <td><a href="https://pan.baidu.com/s/1ayoXyLkMCbkEh9r1TwX32Q">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="https://pan.baidu.com/s/1m4Yppo2JpV4_0qZazPqcFw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1-_UB1CV96WQN0yp3v9kcOA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/12YZmPb8fZZwOzn9kI6hb0g">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>People's Daily News 人民日报</td>
      <td><a href="https://pan.baidu.com/s/1FN2BpELh1jzebnr4q0_60A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1mHkVFJkdYQkzrf_-yzxIhg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1WW2tlEdQBufjj9ubWFICHg">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="https://pan.baidu.com/s/19FJqCtYWBU4SZUYmCzegvA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/13N7yFouswT1c9nng57sbDg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1crPFyGwR5YHA33C5R_WTpQ">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="https://pan.baidu.com/s/1FZBtQJh4LzSzSrwGcT7mpA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1jUCSuOFqgbY_DCWV6WwgxQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1TQ8tWlGfEFaSutCJVjPLWQ">300d</a></td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="https://pan.baidu.com/s/1Rm9rB2JP9Phm6GrpZVy-Wg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1YzMG8ffRsJZroZltf4Hm9A">300d</a></td>
      <td>300d</td>
      <td>300d</td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书<sup>*</sup></td>
      <td>300d</td>
      <td>300d</td>
      <td>NAN</td>
      <td>NAN</td>
    </tr>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
      <td>300d</td>
    </tr>
</table>

<sup>\*</sup>Character embeddings are provided, since most of Hanzi are words in the archaic Chinese.

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
    <td><a href="https://pan.baidu.com/s/1P_jpFuPI6K36PlmOLvdRJA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1XlOOon_NQtnhSKYbgwXEtA">300d</a></td>
  </tr>

  <tr align="center">
    <td rowspan="3">Ngram</td>
    <td>Word → Ngram (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1C59ebYO14o1otnt3CK5cVA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1gdCpq0nsAhoFxKqctyOtzA">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Ngram (1-3)</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
  <tr align="center">
    <td>Ngram (1-2) → Ngram (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1Fdf4OXZoG138aLZMBsNVnw">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1bMxYF7mwiCi_TQx799FhEQ">300d</a></td>
  </tr>
  
  <tr align="center">
    <td rowspan="3">Character</td>
    <td>Word → Character (1)</td>
 	  <td><a href="https://pan.baidu.com/s/1QoWF_Xe5MQHT0jG8Q95RZg">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1GNdDPjgZuq0ES9xE_ASNxw">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-2)</td>
 	  <td><a href="https://pan.baidu.com/s/1MsNSYjuglTROrojd9Ce2Xg">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1ewUYm01u0K_xrg3tDJ9kDw">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-4)</td>
    <td><a href="https://pan.baidu.com/s/1JAfw3-NQoWmSKiwDrCJXhg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1t2q8xLxljgy6ekOwNZaKeA">300d</a></td>
  </tr>
  
  <tr align="center">
  	<td rowspan="1">Radical</td>
    <td>Radical</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
  
  <tr align="center">
    <td rowspan="2">Position</td>
    <td>Word → Word (left/right)</td>
    <td><a href="https://pan.baidu.com/s/1bS-T-pXJCOxueuE-PDbYpA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1_jOOm6YxZhBEjPL5aP8ezQ">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Word (distance)</td>
    <td><a href="https://pan.baidu.com/s/1gnoAeaYGQrMWb-etfWSIQA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1DrCNkHJgeh0QBWKWvouboQ">300d</a></td>
  </tr>
  
  <tr align="center">
    <td>Global</td>
    <td>Word → Text</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
    
  <tr align="center">
    <td rowspan="2">Syntactic Feature</td>
    <td>Word → POS</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
  <tr align="center">
    <td>Word → Dependency</td>
    <td>300d</td>
 	  <td>300d</td>
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
		<td>4.1G</td>
		<td>745M</td>
		<td>5422K</td>
		<td>Chinese Encyclopedia data from<br />https://baike.baidu.com/</td>
	</tr>
	<tr align="center">
		<td>Wikipedia_zh<br />中文维基百科</td>
		<td>1.3G</td>
		<td>223M</td>
		<td>2129K</td>
		<td>Chinese Wikipedia data from<br />https://dumps.wikimedia.org/</td>
	</tr>
	<tr align="center">
		<td>People's Daily News<br />人民日报</td>
		<td>3.9G</td>
		<td>668M</td>
		<td>1664K</td>
		<td>News data from People's Daily(1946-2017)<br />http://data.people.com.cn/</td>
	</tr>
	<tr align="center">
		<td>Sogou News<br />搜狗新闻</td>
		<td>3.7G</td>
		<td>649M</td>
		<td>1226K</td>
		<td>News data provided by Sogou labs<br />http://www.sogou.com/labs/</td>
	</tr>
  <tr align="center">
    <td>Financial News<br />金融新闻</td>
    <td>6.2G</td>
    <td>1055M</td>
    <td>2785K</td>
    <td>Financial news collected from multiple news websites</td>
  </tr>
	<tr align="center">
		<td>Zhihu_QA<br />知乎问答</td>
		<td>2.1G</td>
		<td>384M</td>
		<td>1117K</td>
		<td>Chinese QA data from<br />https://www.zhihu.com/</td>
	</tr>
	<tr align="center">
		<td>Weibo<br />微博</td>
		<td>0.73G</td>
		<td>136M</td>
		<td>850K</td>
		<td>Chinese microblog data provided by NLPIR Lab<br />http://www.nlpir.org/download/weibo.7z</td>
	</tr>
	<tr align="center">
		<td>Literature<br />文学作品</td>
		<td>0.93G</td>
		<td>177M</td>
		<td>702K</td>
		<td>8599 modern Chinese literature works</td>
	</tr>
	<tr align="center">
		<td>Mixed-large<br />综合</td>
		<td>22.6G</td>
    <td>4037M</td>
    <td>10653K</td>
		<td>We build the large corpus by merging the above corpora.</td>
	</tr>
  <tr align="center">
    <td>Complete Library in Four Sections<br />四库全书</td>
    <td>1.5G</td>
    <td>714M</td>
    <td>21.8K</td>
    <td>The largest collection of texts in pre-modern China.</td>
  </tr>
</table>

All words are concerned, including low frequency words.

## Toolkits
All word vectors are trained by [ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit. Ngram2vec toolkit is a superset of [word2vec](https://github.com/svn2github/word2vec) and [fasttext](https://github.com/facebookresearch/fastText) toolkit, where arbitrary context features and models are supported.

## Chinese Word Analogy Benchmarks
The quality of word vectors is often evaluated by analogy question tasks. In this project, two benchmarks are exploited for evaluation. The first is CA-translated, where most analogy questions are directly translated from English benchmark. Although CA-translated has been widely used in many Chinese word embedding papers, it only contains questions of three semantic questions and covers 134 Chinese words. In contrast, CA8 is specifically designed for Chinese language. It contains 17813 analogy questions and covers comprehensive morphological and semantic relations. The CA-translated, CA8, and their detailed descriptions are provided in [**testsets**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets) folder.


## Evaluation Toolkit
We present an evaluation toolkit in [**evaluation**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/evaluation) folder. 

Run the following codes to evaluate dense vectors.
```
$ python ana_eval_dense.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_dense.py -v <vector.txt> -a CA8/semantic.txt
```
Run the following codes to evaluate sparse vectors.
```
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/semantic.txt
```

## Reference
Please cite the paper, if using these embeddings and CA8 dataset.

Shen Li, Zhe Zhao, Renfen Hu, Wensi Li, Tao Liu, Xiaoyong Du, <em>Analogical Reasoning on Chinese Morphological and Semantic Relations</em>, ACL 2018.

<!-- 
```
@InProceedings{shen2018analogical,
  title={Analogical Reasoning on Chinese Morphological and Semantic Relations},
  author={Shen, Li and Zhe, Zhao and Renfen, Hu and Wensi, Li and Tao, Liu and Xiaoyong, Du},
  year={2018},
}
```
 -->
