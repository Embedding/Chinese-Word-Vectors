# Chinese-Word-Vectors 中文词向量
We provide Chinese word vectors trained by different **representations** (dense and sparse), **context features** (word, ngram, and character), and **corpus**. One can easily reproduce the results reported in the paper by downloading the trained vectors, analogical reasoning datasets, and evaluation sripts. 

### Representations
Existing word representations methods fall into one of the two classes, **dense** and **sparse** represnetations. Word2vec and PPMI are respectively typical methods of these two classes. Word2vec trains low-dimensional real (dense) vectors through shallow neural network. It is also often called neural embedding method. PPMI is a sparse bag-of-features representation weighted by positive-pointwise-mutual-information (PPMI) weighting scheme.

### Context features
Three context features: **word**, **ngram**, and **character** are considered in this work. Most methods learn word representations upon word-word co-occurrence statistics, namely using word as context feature **(word feature)**. Inspired by language modeling problem, we introduce ngram feature into the context. Both word-word and word-bigram co-occurrence statistics are used for training **(ngram feature)**. For Chinese, the character itself conveys strong semantics. We use word-word and word-character co-occurrence statistics to learn word representations. The length of character-level ngrams ranges from 1 to 4 **(character feature)**.

### Corpus
we made great efforts to collect corpus in various domains. Their detailed information is listed as follows:

Corpus | size | Description 
----|----|----
baidu_baike|4.3G|Chinese Baike data from https://baike.baidu.com/
wikipedia_zh|1.2G|Chinese wikipedia data from https://dumps.wikimedia.org/
People's Daily News|3.9G|News data from People's Daily(1946-2017) http://data.people.com.cn/
zhihu_QA|3.6G|Chinese QA data from https://www.zhihu.com/ including 32137 questions and 3239114 answers
literature|0.9G|8599 modern Chinese literature works
Sogou news|3.7G|News data provided by Sougou labs http://www.sogou.com/labs/
mixed-large|17.6G|We create the large corpus by adding the above corpus together
mixed-small|4.3G|Sampled from the mixed-large dataset

All the text data are preprocessed by removing html and xml tags. Only the plain text are kept and HanLP(v_1.5.3) are used for word segmentation. 

### Pre-trained Chinese word vectors  

Corpus/representations-feature | word2vec-word | word2vec-ngram | word2vec-character | PPMI-word | PPMI-ngram | PPMI-character
----|----|----|----|----|----|----
Baidu Baike 百度百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
wikipedia_zh 中文维基百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
People's Daily News 人民日报 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
zhihu_QA 知乎问答 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Literature 文学作品 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Sogou News 搜狗新闻 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-small | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-large | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)

### Toolkits and training protocols
The **word2vec-word** is implemented by [word2vec](https://github.com/svn2github/word2vec) toolikit. The **word2vec-character** is implemented by [fasttext](https://github.com/facebookresearch/fastText) toolkit. The rest are implemented by [ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit.

The detailed training protocols are as follows: the size of dynamic window is set to 5; the dimension is 300; high-frequency words are filtered with sub-sampling at 1e-5 and low-frequency words are removed with threshold at 5. For word2vec model, we use skip-gram with negative sampling. For both word2vec and PPMI, context distribution smoothing (cds) is set to 0.75. 
