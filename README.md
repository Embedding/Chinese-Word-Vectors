# Chinese Word Vectors 中文词向量
This project provides 100+ Chinese Word Vectors (embeddings) trained with different **representations** (dense and sparse), **context features** (word, ngram, character, and more), and **corpora**. One can easily obtain pre-trained vectors with different properties and use them for downstream tasks. 

Moreover, we provide a Chinese analogical reasoning dataset **CA8** and an evaluation toolkit for users to evaluate the quality of their word vectors.

## Reference
Please cite the paper, if using these embeddings and CA8 dataset.

Shen Li, Zhe Zhao, Renfen Hu, Wensi Li, Tao Liu, Xiaoyong Du, <a href="http://aclweb.org/anthology/P18-2023"><em>Analogical Reasoning on Chinese Morphological and Semantic Relations</em></a>, ACL 2018.

```
@InProceedings{P18-2023,
  author =  "Li, Shen
    and Zhao, Zhe
    and Hu, Renfen
    and Li, Wensi
    and Liu, Tao
    and Du, Xiaoyong",
  title =   "Analogical Reasoning on Chinese Morphological and Semantic Relations",
  booktitle =   "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
  year =  "2018",
  publisher =   "Association for Computational Linguistics",
  pages =   "138--143",
  location =  "Melbourne, Australia",
  url =   "http://aclweb.org/anthology/P18-2023"
}
```

&nbsp;

A detailed analysis of the relation between the intrinsic and extrinsic evaluations of Chinese word embeddings is shown in the paper:

Yuanyuan Qiu, Hongzheng Li, Shen Li, Yingdi Jiang, Renfen Hu, Lijiao Yang. <a href="http://www.cips-cl.org/static/anthology/CCL-2018/CCL-18-086.pdf"><em>Revisiting Correlations between Intrinsic and Extrinsic Evaluations of Word Embeddings</em></a>. Chinese Computational Linguistics and Natural Language Processing Based on Naturally Annotated Big Data. Springer, Cham, 2018. 209-221. (CCL & NLP-NABD 2018 Best Paper)

```
@incollection{qiu2018revisiting,
  title={Revisiting Correlations between Intrinsic and Extrinsic Evaluations of Word Embeddings},
  author={Qiu, Yuanyuan and Li, Hongzheng and Li, Shen and Jiang, Yingdi and Hu, Renfen and Yang, Lijiao},
  booktitle={Chinese Computational Linguistics and Natural Language Processing Based on Naturally Annotated Big Data},
  pages={209--221},
  year={2018},
  publisher={Springer}
}
```

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
    <td><b>Negative Sampling<sup>*</sup></b></td>
  </tr>
  <tr align="center">
    <td>5</td>
    <td>Yes</td>
    <td>1e-5</td>
    <td>10</td>
    <td>5</td>
    <td>5</td>
  </tr>
</table>

<sup>\*</sup>Only for SGNS.

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
      <td><a href="https://pan.baidu.com/s/1Rn7LtTH0n7SHyHPfjRHbkg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1XEmP_0FkQwOjipCjI2OPEw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1eeCS7uD3e_qVN8rPwmXhAw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1Gndr0fReIq_oJ3R34CxlPg">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="https://pan.baidu.com/s/1AmXYWVgkxrG4GokevPtNgA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1ZKePwxwsDdzNrfkc6WKdGQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1ZBVVD4mUSUuXOxlZ3V71ZA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/19wQrclyynOnco3JBvnI5pA">300d</td>
    </tr>
    <tr  align="center">
      <td>People's Daily News 人民日报</td>
      <td><a href="https://pan.baidu.com/s/19sqMz-JAhhxh3o6ecvQxQw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1upPkA8KJnxTZBfjuNDtaeQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1BvKk2QjbtQMch7EISppW2A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/19Vso_k79FZb5OZCWQPAnFQ">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="https://pan.baidu.com/s/1tUghuTno5yOvOx4LXA9-wg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/13yVrXeGYkxdGW3P6juiQmA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1pUqyn7mnPcUmzxT64gGpSw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1svFOwFBKnnlsqrF1t99Lnw">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td><a href="https://pan.baidu.com/s/1EhtsbDa3ekzZPODWNLHcXA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1FcPHv7S4vUgnL7WeWf4_PA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/13CAxY5ffRFuOcHZu8VmArw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1sqvrUtGBAZ7YWEsGz41DRQ">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="https://pan.baidu.com/s/1VGOs0RH7DXE5vRrtw6boQA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1OQ6fQLCgqT43WTwh5fh_lg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1_xogqF9kJT6tmQHSAYrYeg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1Fo27Lv_0nz8FXg-xbOz14Q">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td><a href="https://pan.baidu.com/s/1zbuUJEEEpZRNHxZ7Gezzmw">300d</a></td>
      <td><a href="https://pan.baidu.com/s/11PWBcvruXEDvKf2TiIXntg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/10bhJpaXMCUK02nHvRAttqA">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1FHl_bQkYucvVk-j2KG4dxA">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="https://pan.baidu.com/s/1ciq8iXtcrHpu3ir_VhK0zg">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1manrKRDb64t4QnlfIEIF-A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1IG8IxNp2s7vVklz-vyZR9A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1pDiUKNpas1Gpzip-sFlh2w">300d</a></td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书<sup>*</sup></td>
      <td><a href="https://pan.baidu.com/s/1vPSeUsSiWYXEWAuokLR0qQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1sS9E7sclvS_UZcBgHN7xLQ">300d</a></td>
      <td>NAN</td>
      <td>NAN</td>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合<br>Baidu Netdisk / Google Drive</td>
      <td>
        <a href="https://pan.baidu.com/s/1luy-GlTdqqvJ3j-A4FcIOw">300d</a><br>
        <a href="https://drive.google.com/open?id=1Zh9ZCEu8_eSQ-qkYVQufQDNKPC4mtEKR">300d</a>
      </td>
      <td>
        <a href="https://pan.baidu.com/s/1oJol-GaRMk4-8Ejpzxo6Gw">300d</a><br>
        <a href="https://drive.google.com/open?id=1WUU9LnoAjs--1E_WqcghLJ-Pp8bb38oS">300d</a>
      </td>
      <td>
        <a href="https://pan.baidu.com/s/1DjIGENlhRbsVyHW-caRePg">300d</a><br>
        <a href="https://drive.google.com/open?id=1aVAK0Z2E5DkdIH6-JHbiWSL5dbAcz6c3">300d</a>
      </td>
      <td>
        <a href="https://pan.baidu.com/s/14JP1gD7hcmsWdSpTvA3vKA">300d</a><br>
        <a href="https://drive.google.com/open?id=1kSAl4_AOg3_6ayU7KRM0Nk66uGdSZdnk">300d</a>
      </td>
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
      <td><a href="https://pan.baidu.com/s/1_itcjrQawCwcURa7WZLPOA">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1cEZzN1S2senwWSyHOnL7YQ">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1KcfFdyO0-kE9S9CwzIisfw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1FXYM3CY161_4QMgiH8vasQ">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Wikipedia_zh 中文维基百科</td>
      <td><a href="https://pan.baidu.com/s/1MGXRrc54nITPzQ7sfEUjMA">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1mtxZna8UJ7xBIxhBFntumQ">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1dDImpAx41V73Byl2julOGA">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1bsBQHXFpxMHGBexYof1_rw">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>People's Daily News 人民日报</td>
      <td><a href="https://pan.baidu.com/s/1NLr1K7aapU2sYBvzbVny5g">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1LJl3Br0ccGDHP0XX2k3pVw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1GQQXGMn1AHh-BlifT0JD2g">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1Xm9Ec3O3rJ6ayrwVwonC7g">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Sogou News 搜狗新闻</td>
      <td><a href="https://pan.baidu.com/s/1ECA51CZLp9_JB_me7YZ9-Q">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1FO39ZYy1mStERf_b53Y_yQ">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1lLBFBk8nn3spFAvKY9IJ6A">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1f-dLQZlZo_-B5ZKcPIc6rw">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Financial News 金融新闻</td>
      <td><a href="https://pan.baidu.com/s/10wtgdmrTsTrjpSDvI0KzOw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1b6zjvhOIqTdACSSbriisVw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1w24vCfgqcoJvPxsB5VrRvw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1b9BPiDRhiEZ-6ybTcovrqQ">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Zhihu_QA 知乎问答 </td>
      <td><a href="https://pan.baidu.com/s/1VaUP3YJC0IZKTbJ-1_8HZg">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1g39PKwT0kSmpneKOgXR5YQ">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1d8Bsuak0fyXxQOVUiNr-2w">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1D5fteBX0Vy4czEqpxXjlrQ">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Weibo 微博</td>
      <td><a href="https://pan.baidu.com/s/15O2EbToOzjNSkzJwAOk_Ug">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/11Dqywn0hfMhysto7bZS1Dw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1wY-7mfV6nwDj_tru6W9h4Q">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1DMW-MgLApbQnWwDd-pT_qw">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Literature 文学作品</td>
      <td><a href="https://pan.baidu.com/s/1HTHhlr8zvzhTwed7dO0sDg">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1jAuGJBxKqgapt__urGsBOQ">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/173AJfCoAV0ZA8Z31tKBdTA">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1dFCxke_Su3lLsuwZr7co3A">Sparse</a></td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书<sup>*</sup></td>
      <td><a href="https://pan.baidu.com/s/1NJ1Gc99oE0-GV0QxBqy-qw">Sparse</a></td>
      <td><a href="https://pan.baidu.com/s/1YGEgyXIbw0O4NtoM1ohjdA">Sparse</a></td>
      <td>NAN</td>
      <td>NAN</td>
    </tr>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合</td>
      <td>Sparse</td>
      <td>Sparse</td>
      <td>Sparse</td>
      <td>Sparse</td>
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
    <td><a href="https://pan.baidu.com/s/1Rn7LtTH0n7SHyHPfjRHbkg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/18T6DRVmS_cZu5u64EbbESQ">300d</a></td>
  </tr>

  <tr align="center">
    <td rowspan="3">Ngram</td>
    <td>Word → Ngram (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1XEmP_0FkQwOjipCjI2OPEw">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/12asujjAaaqxNFYRNP-MThw">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Ngram (1-3)</td>
    <td><a href="https://pan.baidu.com/s/1oUmbxsnSuXf2jU8Jxu7U8A">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1ylg6FfFHa0kXbiVz8bIL8g">300d</a></td>
  </tr>
  <tr align="center">
    <td>Ngram (1-2) → Ngram (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1Za7DIGVhE6dMsTmxHb-izg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1oKI4Cs9eo7bg5mqfY1hdmg">300d</a></td>
  </tr>
  
  <tr align="center">
    <td rowspan="3">Character</td>
    <td>Word → Character (1)</td>
 	  <td><a href="https://pan.baidu.com/s/1c9yiosHKNIZwRlLzD_F1ig">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1KGZ_x8r-lq-AuElLCSVzvQ">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-2)</td>
 	  <td><a href="https://pan.baidu.com/s/1eeCS7uD3e_qVN8rPwmXhAw">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1q0ItLzbn5Tfb3LhepRCeEA">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Character (1-4)</td>
    <td><a href="https://pan.baidu.com/s/1WNWAnba56Rqjmx-FAN_7_g">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1hJKTAz6PwS7wmz9wQgmYeg">300d</a></td>
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
    <td><a href="https://pan.baidu.com/s/1JvjcrXFZPknT5H5Xw6KRVg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1m6K9CnIIS8FrQZdDuF6hPQ">300d</a></td>
  </tr>
  <tr align="center">
    <td>Word → Word (distance)</td>
    <td><a href="https://pan.baidu.com/s/1c29BDu4R1hyUX-sgvlHJnA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1sMZHIc-7eU6gRalHwtBHZw">300d</a></td>
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
We made great efforts to collect corpus across various domains. All text data are preprocessed by removing html and xml tags. Only the plain text are kept and [HanLP(v_1.5.3)](https://github.com/hankcs/HanLP) is used for word segmentation. In addition, traditional Chinese characters are converted into simplified characters with [Open Chinese Convert (OpenCC)](https://github.com/BYVoid/OpenCC). The detailed corpora information is listed as follows:

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
		<td>Chinese microblog data provided by NLPIR Lab<br />http://www.nlpir.org/wordpress/download/weibo.7z</td>
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
