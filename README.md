# Chinese-Word-Vectors 中文词向量
We provide Chinese word vectors trained by different **representations** (dense and sparse), **context features** (word, ngram, and character), and **corpora**. One can easily reproduce the results reported in the paper by downloading the trained vectors, analogical reasoning datasets, and evaluation scripts. 

### Representations
Existing word representations methods fall into one of the two classes, **dense** and **sparse** represnetations. Word2vec and PPMI are respectively typical methods of these two classes. Word2vec trains low-dimensional real (dense) vectors through shallow neural network. It is also often called neural embedding method. PPMI is a sparse bag-of-features representation weighted by positive-pointwise-mutual-information (PPMI) weighting scheme.

### Context features
Three context features: **word**, **ngram**, and **character** are considered in this work. Most methods learn word representations upon word-word co-occurrence statistics, namely using word as context feature **(word feature)**. Inspired by language modeling problem, we introduce ngram feature into the context. Both word-word and word-bigram co-occurrence statistics are used for training **(ngram feature)**. For Chinese, the character itself conveys strong semantics. We use word-word and word-character co-occurrence statistics to learn word representations. The length of character-level ngrams ranges from 1 to 4 **(character feature)**.

### Corpus
we made great efforts to collect corpus in various domains. The experimental results show that the corpus domain has substantial influence on word vectors' properties. The detailed corpora information is listed as follows:

Corpus | size | Description 
----|----|----
baidu_baike 百度百科|4.3G|Chinese Baike data from https://baike.baidu.com/
wikipedia_zh 中文维基百科|1.2G|Chinese wikipedia data from https://dumps.wikimedia.org/
People's Daily News 人民日报|3.9G|News data from People's Daily(1946-2017) http://data.people.com.cn/
Sogou news 搜狗新闻|3.7G|News data provided by Sogou labs http://www.sogou.com/labs/
zhihu_QA 知乎问答|3.6G|Chinese QA data from https://www.zhihu.com/ including 32137 questions and 3239114 answers
literature 文学作品|0.9G|8599 modern Chinese literature works
The Four Categories 四库全书| |
Weibo 微博| | https://weibo.com/
mixed-large|17.6G|We build the large corpus by merging the above corpora

All the text data are preprocessed by removing html and xml tags. Only the plain text are kept and HanLP(v_1.5.3) are used for word segmentation. 

### Pre-trained Chinese word vectors  

Corpus/representations-feature | word2vec-word | word2vec-ngram | word2vec-character | PPMI-word | PPMI-ngram | PPMI-character
----|----|----|----|----|----|----
Baidu Baike 百度百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
wikipedia_zh 中文维基百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
People's Daily News 人民日报 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Sogou News 搜狗新闻 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
zhihu_QA 知乎问答 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Literature 文学作品 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-large | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-small | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)


<table>
  <tr>
    <th>Feature</th>
    <th>Co-occurrence type</th>
    <th>Pre-trained word vectors</th>
  </tr>
  <tr>
    <td> word </td>
    <td> word-word </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  <tr>
    <td rowspan="3"> ngram </td>
    <td> word-bigram </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
    <td> word-trigram </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  <tr>
    <td> bigram-bigram </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  
  <tr>
    <td rowspan="3"> character </td>
    <td> word-character (1) </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
    <td> word-character (1-2) </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  <tr>
    <td> word-character (1-4) </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  
  <tr>
    <td> radical </td>
    <td> radical </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
  
  <tr>
    <td rowspan="2"> position </td>
    <td> word-word(left/right) (1) </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
    <td> word-word(distance) </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
  
  <tr>
    <td> global </td>
    <td> word-text </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
    
  <tr>
    <td rowspan="2"> syntactic feature </td>
    <td> word-POS </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  <tr>
    <td> word-dependency </td>
    <td> <a href="http://www.baidu.com">target</a>; <a href="http://www.baidu.com">context</a> </td>
  </tr>
    
</table>



### Toolkits and training protocols
The **word2vec-word** is implemented by [word2vec](https://github.com/svn2github/word2vec) toolikit. The **word2vec-character** is implemented by [fasttext](https://github.com/facebookresearch/fastText) toolkit. The rest are implemented by [ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit.

The detailed training protocols are as follows: the size of dynamic window is set to 5; the dimension is 300; high-frequency words are filtered with sub-sampling at 1e-5 and low-frequency words are removed with threshold at 5. For word2vec model, we use skip-gram with negative sampling. For both word2vec and PPMI, context distribution smoothing (cds) is set to 0.75. 
