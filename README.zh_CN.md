# Chinese Word Vectors 中文词向量
本项目提供了100多个中文单词向量（嵌入），这些向量使用不同的**表征方式**（密集和稀疏）、**上下文特征**（单词、ngram、字符等）和**语料库**进行训练。您可以很容易地获得具有不同属性的预训练向量，并将其用于下游任务。

此外，我们还提供了一个中文类比推理数据集**CA8**和一个评估工具，供用户评估其词向量的质量。

## 引用参考
如果您使用了这些嵌入和CA8数据集，请引用本文。

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

汉语词语嵌入的内在和外在评估之间的关系的详细分析：

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

## 格式
预先训练的矢量文件是文本格式的。每行包含一个单词及其向量。每个值用空格隔开。第一行记录元信息：第一行数字表示文件中的字数，第二行表示维度大小。

除了密集词向量（用SGNS训练），我们还提供稀疏向量（用PPMI训练）。它们的格式与liblinear相同，其中“:”之前的数字表示维度索引，“:”之后的数字表示值。

## 预训练的汉语词向量

### 基本设置

<table>
  <tr align="center">
    <td><b>窗口大小</b></td>
    <td><b>动态窗口</b></td>
    <td><b>Sub-sampling</b></td>
    <td><b>低频词</b></td>
    <td><b>迭代数</b></td>
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

<sup>\*</sup>仅适用于SGNS。

### 多个领域的词向量

训练不同表征、语境特征和语料库的汉语词向量。

<table align="center">
    <tr align="center">
        <td colspan="5"><b>Word2vec / Skip-Gram  Negative Sampling (SGNS)</b></td>
    </tr>
    <tr align="center">
        <td rowspan="2">语料库</td>
        <td colspan="4">上下文特征</td>
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
      <td><a href="https://pan.baidu.com/s/1IiIbQGJ_AooTj5s8aZYcvA">300d</a> / PWD: 5555</td>
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
      <td><a href="https://pan.baidu.com/s/1Oa4CkPd8o2xd6LEAaa4gmg">300d</a> / PWD: z5b4</td>
      <td><a href="https://pan.baidu.com/s/1IG8IxNp2s7vVklz-vyZR9A">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1SEOKrJYS14HpqIaQT462kA">300d</a> / PWD: yenb</td>
    </tr>
    <tr  align="center">
      <td>Complete Library in Four Sections<br />四库全书<sup>*</sup></td>
      <td><a href="https://pan.baidu.com/s/1vPSeUsSiWYXEWAuokLR0qQ">300d</a></td>
      <td><a href="https://pan.baidu.com/s/1sS9E7sclvS_UZcBgHN7xLQ">300d</a></td>
      <td>NAN</td>
      <td>NAN</td>
    </tr>
    <tr  align="center">
      <td>Mixed-large 综合<br>百度网盘 / Google Drive</td>
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
        <td colspan="5"><b>正点互信息 Positive Pointwise Mutual Information (PPMI)</b></td>
    </tr>
    <tr align="center">
        <td rowspan="2">语料库</td>
        <td colspan="4">上下文特征</td>
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

<sup>\*</sup>提供了字符嵌入，因为大多数汉字都是古汉语中的单词。

### 各种共现信息

我们根据不同的共现统计数据发布了多种词向量。在相关文献中，目标向量和上下文向量通常被称为输入向量和输出向量。

在这一部分中，您可以获得单词以外的任意语言单位的向量。例如，字符向量是word-character的上下文向量。

所有词向量均由基于百度百科的SGNS进行训练。

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

## 表征
现有的词表示方法分为两类，**密集**和**稀疏**表示。SGNS模型（word2vec toolkit中的模型）和PPMI模型分别是这两个类的典型方法。SGNS模型通过浅层神经网络训练低维实（密）向量。又称神经网络嵌入法。PPMI模型是一种稀疏的特征表示包，采用正的逐点互信息（PPMI）加权方案进行加权。

## 上下文特征
三个上下文特征：**单词**，**ngram**，和**字符**，在单词嵌入文献中是常用的。大多数词表示方法本质上利用 单词-单词 共现统计，即使用词作为上下文特征 **（词特征）**。受语言建模问题的启发，我们将ngram特征引入到上下文中。单词和单词ngram共现统计都用于训练 **（ngram特征）**。对于中文来说，汉字常常传达强烈的语义。为此，我们考虑使用 单词-单词 和 单词-字符 共现统计来学习单词向量。字符级ngram的长度范围为1到4 **（字符特征）**。

除了单词、ngram和字符外，还有其他一些特征对单词向量的性质有很大的影响。例如，使用整个文本作为上下文特征可以在词向量中引入更多的主题信息；使用依赖分析作为上下文特征可以在词向量中添加语法约束。本项目共考虑了17种共现类型。

## 语料库
我们努力收集跨领域的语料库。所有文本数据都通过删除html和xml标记进行预处理。只保留纯文本和[HanLP（v_1.5.3）](https://github.com/hankcs/HanLP)用于分词。此外，繁体汉字通过[Open Chinese Convert（OpenCC）](https://github.com/BYVoid/OpenCC). 具体语料库信息如下：

<table>
	<tr align="center">
		<td><b>语料库</b></td>
		<td><b>大小</b></td>
		<td><b>Tokens</b></td>
		<td><b>词汇量</b></td>
		<td><b>说明</b></td>
	</tr>
	<tr align="center">
		<td>Baidu Encyclopedia<br />百度百科</td>
		<td>4.1G</td>
		<td>745M</td>
		<td>5422K</td>
		<td>中国百科全书资料<br />https://baike.baidu.com/</td>
	</tr>
	<tr align="center">
		<td>Wikipedia_zh<br />中文维基百科</td>
		<td>1.3G</td>
		<td>223M</td>
		<td>2129K</td>
		<td>中国维基百科数据<br />https://dumps.wikimedia.org/</td>
	</tr>
	<tr align="center">
		<td>People's Daily News<br />人民日报</td>
		<td>3.9G</td>
		<td>668M</td>
		<td>1664K</td>
		<td>《人民日报》新闻资料（1946-2017）<br />http://data.people.com.cn/</td>
	</tr>
	<tr align="center">
		<td>Sogou News<br />搜狗新闻</td>
		<td>3.7G</td>
		<td>649M</td>
		<td>1226K</td>
		<td>搜狗实验室提供的新闻数据<br />http://www.sogou.com/labs/</td>
	</tr>
  <tr align="center">
    <td>Financial News<br />金融新闻</td>
    <td>6.2G</td>
    <td>1055M</td>
    <td>2785K</td>
    <td>从多个新闻网站收集的财经新闻</td>
  </tr>
	<tr align="center">
		<td>Zhihu_QA<br />知乎问答</td>
		<td>2.1G</td>
		<td>384M</td>
		<td>1117K</td>
		<td>中国问答类型数据来自<br />https://www.zhihu.com/</td>
	</tr>
	<tr align="center">
		<td>Weibo<br />微博</td>
		<td>0.73G</td>
		<td>136M</td>
		<td>850K</td>
		<td>NLPIR实验室提供的中文微博数据<br />http://www.nlpir.org/wordpress/download/weibo.7z</td>
	</tr>
	<tr align="center">
		<td>Literature<br />文学作品</td>
		<td>0.93G</td>
		<td>177M</td>
		<td>702K</td>
		<td>8599部中国现代文学作品</td>
	</tr>
	<tr align="center">
		<td>Mixed-large<br />综合</td>
		<td>22.6G</td>
    <td>4037M</td>
    <td>10653K</td>
		<td>我们通过合并上述语料库来构建大型语料库。</td>
	</tr>
  <tr align="center">
    <td>Complete Library in Four Sections<br />四库全书</td>
    <td>1.5G</td>
    <td>714M</td>
    <td>21.8K</td>
    <td>中国古代最大的著作收藏。</td>
  </tr>
</table>

所有的词都有被关注到，包括低频词。

## Toolkits
所有的词向量都由[ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit训练. Ngram2vec toolkit是[word2vec](https://github.com/svn2github/word2vec) 和 [fasttext](https://github.com/facebookresearch/fastText) toolkit的超集，其中支持任意上下文功能和模型。

## 汉语词语类比基准
词向量的质量通常通过类比问题任务来评估。在这个项目中，利用两个基准进行评估。第一种是CA翻译，大多数类比问题直接从英语基准翻译而来。虽然CA翻译在许多汉语嵌词论文中得到了广泛的应用，但它只包含三个语义问题，涵盖了134个汉语单词。相比之下，CA8是专门为中文设计的。它包含17813个类比问题，涵盖了全面的形态和语义关系。CA8及其详细描述见[**testsets**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets)文件夹。

## 评估工具包
我们在[**evaluation**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/evaluation)文件夹中提供了一个评估工具包。

运行以下代码来评估密集向量。
```
$ python ana_eval_dense.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_dense.py -v <vector.txt> -a CA8/semantic.txt
```
运行以下代码来评估稀疏向量。
```
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/semantic.txt
```
