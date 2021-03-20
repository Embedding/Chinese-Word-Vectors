# Chinese Word Vectors 中文词向量
[For English](https://github.com/Embedding/Chinese-Word-Vectors/blob/master/README.md)

本项目提供超过100种中文词向量，其中包括不同的表示方式（稠密和稀疏）、不同的上下文特征（词、N元组、字等等）、以及不同的训练语料。获取预训练词向量非常方便，下载后即可用于下游任务。

此外，我们还提供了中文词类比任务数据集**CA8**和配套的评测工具，以便对中文词向量进行评估。

## 参考文献
如果使用了本项目的词向量和CA8数据集请进行如下引用：

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

我们对中文词向量的内部和外部评估任务做了一个非常详尽的分析和对比，参见：

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
所有的预训练词向量文件均为文本格式。每一行都包括一个词和它对应的词向量。所有的值均用空格分开。每个文件的第一行记录了基本信息：第一个数值是文件中总词数，第二个数值是向量维度。

除了稠密的词向量（用SGNS方式训练的），我们也提供了稀疏的词向量（用PPMI方式训练的）。稀疏的词向量格式同liblinear中的一样，以“位置:数值”的方式存储。

## 预训练中文词向量

### 基本参数

<table align="center">
  <tr align="center">
    <td><b>窗口大小</b></td>
    <td><b>动态窗口</b></td>
    <td><b>子采样</b></td>
    <td><b>低频词阈值</b></td>
    <td><b>迭代次数</b></td>
    <td><b>负采样<sup>*</sup></b></td>
  </tr>
  <tr align="center">
    <td>5</td>
    <td>是</td>
    <td>1e-5</td>
    <td>10</td>
    <td>5</td>
    <td>5</td>
  </tr>
</table>

<sup>\*</sup>仅适用于SGNS.

### 不同领域

下列词向量基于不同的表示方式、不同的上下文特征以及不同领域的语料训练而成。

<table align="center">
    <tr align="center">
        <td colspan="5"><b>Word2vec / Skip-Gram with Negative Sampling (SGNS)</b></td>
    </tr>
    <tr align="center">
        <td rowspan="2">语料</td>
        <td colspan="4">上下文特征</td>
    </tr>
    <tr  align="center">
      <td>词</td>
      <td>词 + N元组</td>
      <td>词 + 字</td>
      <td>词 + 字 + N元组</td>
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
        <td rowspan="2">语料</td>
        <td colspan="4">上下文特征</td>
    </tr>
    <tr  align="center">
      <td>词</td>
      <td>词 + N元组</td>
      <td>词 + 字</td>
      <td>词 + 字 + N元组</td>
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

<sup>\*</sup>由于古汉语中绝大部份词均为单字词，因此只需字向量。

### 不同的上下文共现信息

我们提供了基于不同共现信息训练而成的词向量。下述提到的中心向量和上下文向量在类似的论文中也被称为输入和输出向量。

这个部分中的向量不仅仅是词向量，还有其它的语言单位对应的向量。比如，在上下文是“词-字”的条件下，上下文向量会包含字向量。

所有的向量均采用SGNS在百度百科语料上训练而成。

<table align="center">
  <tr align="center">
    <td><b>特征</b></td>
    <td><b>共现信息</b></td>
    <td><b>中心向量</b></td>
    <td><b>上下文向量</b></td>
  </tr>
  
  <tr align="center">
  	<td rowspan="1">词</td>
    <td>词 → 词</td>
    <td><a href="https://pan.baidu.com/s/1Rn7LtTH0n7SHyHPfjRHbkg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/18T6DRVmS_cZu5u64EbbESQ">300d</a></td>
  </tr>

  <tr align="center">
    <td rowspan="3">N元组</td>
    <td>词 → N元组 (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1XEmP_0FkQwOjipCjI2OPEw">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/12asujjAaaqxNFYRNP-MThw">300d</a></td>
  </tr>
  <tr align="center">
    <td>词 → N元组 (1-3)</td>
    <td><a href="https://pan.baidu.com/s/1oUmbxsnSuXf2jU8Jxu7U8A">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1ylg6FfFHa0kXbiVz8bIL8g">300d</a></td>
  </tr>
  <tr align="center">
    <td>N元组 (1-2) → N元组 (1-2)</td>
    <td><a href="https://pan.baidu.com/s/1Za7DIGVhE6dMsTmxHb-izg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1oKI4Cs9eo7bg5mqfY1hdmg">300d</a></td>
  </tr>
  
  <tr align="center">
    <td rowspan="3">字</td>
    <td>词 → 字 (1)</td>
 	  <td><a href="https://pan.baidu.com/s/1c9yiosHKNIZwRlLzD_F1ig">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1KGZ_x8r-lq-AuElLCSVzvQ">300d</a></td>
  </tr>
  <tr align="center">
    <td>词 → 字 (1-2)</td>
 	  <td><a href="https://pan.baidu.com/s/1eeCS7uD3e_qVN8rPwmXhAw">300d</a></td>
    <td><a href="https://pan.baidu.com/s/1q0ItLzbn5Tfb3LhepRCeEA">300d</a></td>
  </tr>
  <tr align="center">
    <td>词 → 字 (1-4)</td>
    <td><a href="https://pan.baidu.com/s/1WNWAnba56Rqjmx-FAN_7_g">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1hJKTAz6PwS7wmz9wQgmYeg">300d</a></td>
  </tr>
  
  <tr align="center">
  	<td rowspan="1">偏旁部首</td>
    <td>偏旁部首</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
  
  <tr align="center">
    <td rowspan="2">位置</td>
    <td>词 → 词 (左/右)</td>
    <td><a href="https://pan.baidu.com/s/1JvjcrXFZPknT5H5Xw6KRVg">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1m6K9CnIIS8FrQZdDuF6hPQ">300d</a></td>
  </tr>
  <tr align="center">
    <td>词 → 词 (距离)</td>
    <td><a href="https://pan.baidu.com/s/1c29BDu4R1hyUX-sgvlHJnA">300d</a></td>
 	  <td><a href="https://pan.baidu.com/s/1sMZHIc-7eU6gRalHwtBHZw">300d</a></td>
  </tr>
  
  <tr align="center">
    <td>全局信息</td>
    <td>词 → 文章</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
    
  <tr align="center">
    <td rowspan="2">语法特征</td>
    <td>词 → 词性</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
  <tr align="center">
    <td>词 → 依存关系</td>
    <td>300d</td>
 	  <td>300d</td>
  </tr>
</table>

## 表示方式
目前有两种词向量的表示方式：**稠密**和**稀疏**的表示方式。SGNS模型（word2vec中提出的一种模型）和PPMI模型分别是二者的代表。SGNS是通过浅层神经网络训练而成的一种低维实向量来表示词语。它通常也被称之为神经词嵌入方法。PPMI模型是一种基于正值逐点互信息并且以稀疏方式表示的特征汇总模型。

## 上下文特征
在词向量领域通常有三种主要的上下文特征：**词**、**N元组**、**字**。大部分词表示方式本质上都是在利用词和词的共现统计信息，换句话说就是把词来当作上下文特征，即上文**词特征**中的向量。受到语言模型的启发，我们将N元组信息也引入了上下文特征中。不只是词和词的共现信息，词和N元组的共现信息也被用在了上文**N元组特征**向量的训练中。对于中文来说，汉字承载了较强的含义，因此我们利用了词和词的共现信息以及词和字的共现信息来训练了一些向量。在上文**字特征**中的向量包括了长度1至4的字级别N元组。

除了词、N元组和字以外。还有一些特征对词向量的性质有重要的影响。比如，把整篇文本作为特征引入训练中会使得词向量受到文章主题的影响；用依存分析的结果作为上下文特征来训练词向量会让词向量受到语法的影响。本项目共涉及17种不同的共现信息。

## 语料
我们花费了大量精力来收集了来自多个领域的语料。所有的文本数据均移除了html和xml标记，仅保留了纯文本。之后采用了[HanLP(v_1.5.3)](https://github.com/hankcs/HanLP)对文本进行了分词。此外，我们将繁体中文用[Open Chinese Convert (OpenCC)](https://github.com/BYVoid/OpenCC)转换为了简体中文。更详细的语料信息如下所示：

<table align="center">
	<tr align="center">
		<td><b>语料</b></td>
		<td><b>大小</b></td>
		<td><b>词数量</b></td>
		<td><b>词汇量</b></td>
		<td><b>详情</b></td>
	</tr>
	<tr align="center">
		<td>Baidu Encyclopedia<br />百度百科</td>
		<td>4.1G</td>
		<td>745M</td>
		<td>5422K</td>
		<td>中文百科<br />https://baike.baidu.com/</td>
	</tr>
	<tr align="center">
		<td>Wikipedia_zh<br />中文维基百科</td>
		<td>1.3G</td>
		<td>223M</td>
		<td>2129K</td>
		<td>中文维基百科<br />https://dumps.wikimedia.org/</td>
	</tr>
	<tr align="center">
		<td>People's Daily News<br />人民日报</td>
		<td>3.9G</td>
		<td>668M</td>
		<td>1664K</td>
		<td>人民日报新闻数据(1946-2017)<br />http://data.people.com.cn/</td>
	</tr>
	<tr align="center">
		<td>Sogou News<br />搜狗新闻</td>
		<td>3.7G</td>
		<td>649M</td>
		<td>1226K</td>
		<td>Sogou labs的新闻数据<br />http://www.sogou.com/labs/</td>
	</tr>
  <tr align="center">
    <td>Financial News<br />金融新闻</td>
    <td>6.2G</td>
    <td>1055M</td>
    <td>2785K</td>
    <td>从多个网站收集到的金融新闻</td>
  </tr>
	<tr align="center">
		<td>Zhihu_QA<br />知乎问答</td>
		<td>2.1G</td>
		<td>384M</td>
		<td>1117K</td>
		<td>中文问答数据<br />https://www.zhihu.com/</td>
	</tr>
	<tr align="center">
		<td>Weibo<br />微博</td>
		<td>0.73G</td>
		<td>136M</td>
		<td>850K</td>
		<td>NLPIR Lab提供的微博数据<br />http://www.nlpir.org/wordpress/download/weibo.7z</td>
	</tr>
	<tr align="center">
		<td>Literature<br />文学作品</td>
		<td>0.93G</td>
		<td>177M</td>
		<td>702K</td>
		<td>8599篇现代文学作品</td>
	</tr>
	<tr align="center">
		<td>Mixed-large<br />综合</td>
		<td>22.6G</td>
    <td>4037M</td>
    <td>10653K</td>
		<td>上述所有数据的汇总</td>
	</tr>
  <tr align="center">
    <td>Complete Library in Four Sections<br />四库全书</td>
    <td>1.5G</td>
    <td>714M</td>
    <td>21.8K</td>
    <td>目前最大的古代文献汇总</td>
  </tr>
</table>

上述统计结果中，所有词都被计算在内，包括低频词。

## 训练工具
所有词向量均采用[ngram2vec](https://github.com/zhezhaoa/ngram2vec/)训练而成。Ngram2vec是[word2vec](https://github.com/svn2github/word2vec)和[fasttext](https://github.com/facebookresearch/fastText)的超集。它可以兼容各种上下文特征并且支持多种模型。

## 中文词类比评测
通常人们利用词类比任务来评测词向量的好坏。本项目中，包含有两个词类比任务。其一是CA-translated，即由英文词类比任务翻译得到的中文词类比任务集。虽然CA-translated被广泛应用于中文词向量相关的论文中，但是它仅仅只有语义相关任务没有语法相关的任务，并且其中词汇量仅有134。因此，我们提供了另一个中文词类比任务集CA8。CA8是特别为中文而设计的词类比任务集。它包括了17813个词类比问题，并且同时涵盖了语法和语义任务。对上述两个数据集更详细的介绍可以参见：[**testsets**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/testsets)文件夹。

## 评测工具
我们提供了配套的评测工具，详见[**evaluation**](https://github.com/Embedding/Chinese-Word-Vectors/tree/master/evaluation)文件夹。

评测稠密的向量，可以运行：
```
$ python ana_eval_dense.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_dense.py -v <vector.txt> -a CA8/semantic.txt
```
评测稀疏的向量，可以运行：
```
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/morphological.txt
$ python ana_eval_sparse.py -v <vector.txt> -a CA8/semantic.txt
```
