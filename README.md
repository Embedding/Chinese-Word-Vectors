# Chinese-Word-Vectors 中文词向量
We are publishing pre-trained Chinese word vectors 
trained on various corpus using word2vec, fastText, GloVe, and ngram2vec toolkits.

### Pre-trained Chinese word vectors for reproducing experimental results reported in the paper 
We provide the word vectors trained by different models (dense and sparse), features (word, ngram, and character), and corpus. One can download the trained vectors to reproduce the results reported in the paper (with analogy evaluation scripts provided in this project). The word2vec-word is implemented by [word2vec](https://github.com/svn2github/word2vec). The word2vec-character is implemented by [fasttext](https://github.com/facebookresearch/fastText). The rest are implemented by [ngram2vec](https://github.com/zhezhaoa/ngram2vec/) toolkit.

Corpus/model-feature | word2vec-word | word2vec-ngram | word2vec-character | PPMI-word | PPMI-ngram | PPMI-character
----|----|----|----|----|----|----
Baidu encyclopedia 百度百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Wikipedia 维基百科 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
People's Daily 人民日报 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Zhihu 知乎 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Literature 文学作品 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
sogou News 搜狗新闻 | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-small | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
Mixed-large | [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com) |  [300](http://www.baidu.com) | [300](http://www.baidu.com) | [300](http://www.baidu.com)
