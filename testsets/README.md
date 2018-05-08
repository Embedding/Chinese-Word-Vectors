# Chinese Word Analogy Benchmarks
The quality of word vectors is often evaluated by analogy question tasks. In this project, two benchmarks are exploited for evaluation. The first is CA-translated ([Chen et al., 2015](#reference)), where most analogy questions are directly translated from English benchmark. Although CA-translated has been widely used in many Chinese word embedding papers, it only contains questions of three semantic questions and covers 134 Chinese words. In contrast, CA8 ([Li et al., 2018](#reference)) is specifically designed for Chinese language. It contains 17813 analogy questions and covers comprehensive morphological and semantic relations.

## CA8

CA8 incorporates comprehensive morphological and semantic relations in Chinese. Specifically, CA8-morphological (CA8-Mor) contains 10177 morphological questions, which are constructed based on two types of relations: reduplication and semi-affixation. CA8-semantic (CA8-Sem) contains 7636 semantic questions, which can be divided into 4 categories and 28 sub-categories. Detailed description is as follows:

<table>
  <tr align="center">
    <td colspan="5"><b>Morphological Questions: Reduplication</b></td>
  </tr>
  <tr align="center">
    <td>Category</td>
    <td>Sub-category</td>
    <td>POS</td>
    <td>Morphological Function</td>
    <td>Example</td>
  </tr>
  <tr align="center">
    <td rowspan="9">A</td>
    <td rowspan="7">AA</td>
    <td rowspan="2">Noun</td>
    <td>Form kinship terms</td>
    <td>爸 (dad) → 爸爸 (dad)</td>
  </tr>
  <tr align="center">
    <td>Yield every / each meaning</td>
    <td>天 (day) → 天天 (everyday)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">Measure</td>
    <td>Yield every / each meaning</td>
    <td>个 (-) → 个个 (every/each)</td>
  </tr>
  <tr align="center">
    <td rowspan="2">Verb</td>
    <td>Signal doing something a little bit</td>
    <td>说 (say) → 说说 (say a little)</td>
  </tr>
  <tr align="center">
    <td>Signal things happen briefly</td>
    <td>看 (look) → 看看 (have a brief look)</td>
  </tr>
  <tr align="center">
    <td rowspan="2">Adjective</td>
    <td>Intensify the adjective</td>
    <td>大 (big) → 大大 (very big)</td>
  </tr>
  <tr align="center">
    <td>Transform it to adverbs</td>
    <td>慢 (slow) → 慢慢 (slowly)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">A yi A</td>
    <td rowspan="1">Verb</td>
    <td>Signal trying to do something</td>
    <td>吃 (eat) → 吃一吃 (try to eat)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">A lai A qu</td>
    <td rowspan="1">Verb</td>
    <td>Signal doing something repeatedly</td>
    <td>飞 (fly) → 飞来飞去 (fly around)</td>
  </tr>
  <tr align="center">
    <td rowspan="9">AB</td>
    <td rowspan="5">AABB</td>
    <td rowspan="1">Noun</td>
    <td>Yield many / much meaning</td>
    <td>山水 (mountain and river) → 山山水水 (many mountains and rivers)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">Verb</td>
    <td>Indicate a continuous action</td>
    <td>说笑 (laugh and chat) → 说说笑笑 (laugh and chat for a while)</td>
  </tr>
  <tr align="center">
    <td rowspan="2">Adjective</td>
    <td>Intensify the adjective</td>
    <td>清楚 (clear) → 清清楚楚 (very clear)</td>
  </tr>
  <tr align="center">
    <td>Yield the meaning of not uniform</td>
    <td>大小 (size) → 大大小小 (all sizes)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">Adverb</td>
    <td>Intensify the adverb</td>
    <td>彻底 (completely) → 彻彻底底 (totally and completely)</td>
  </tr>
  <tr align="center">
    <td rowspan="1">A li A B</td>
    <td rowspan="1">Adjective</td>
    <td>Oralize the adjective and yield derogatory meaning</td>
    <td>慌张 (flurried) → 慌里慌张 (anxious)</td>
  </tr>
  <tr align="center">
    <td rowspan="3">ABAB</td>
    <td rowspan="1">Verb</td>
    <td>Signal doing something a little bit</td>
    <td>注意 (pay attention) → 注意注意 (pay a little attention)</td>
  </tr>
  <tr align="center">
    <td rowspan="2">Adjective</td>
    <td>Intensify the adjective</td>
    <td>雪白 (white) → 雪白雪白 (very white)</td>
  </tr>
  <tr align="center">
    <td>Transform it to a verb</td>
    <td>高兴 (happy) → 高兴高兴 (make someone happy)</td>
  </tr>
</table>

Affixation is a morphological process whereby a bound morpheme (an affix) is attached to roots or stems to form new language units. Chinese is a typical isolating language that has few affixes. [Liu et al. (2001)](#reference) points out that although affixes are rare in Chinese, there are some components behaving like affixes and can also be used as independent lexemes. They are called semi-affixes. We follow their work and adopt this concept.

<table>
  <tr align="center">
    <td colspan="3"><b>Morphological Questions: Semi-affixation</b></td>
  </tr>
  <tr align="center">
    <td>Category</td>
    <td>Semi-affix</td>
    <td>Example</td>
  </tr>
  <tr align="center">
    <td rowspan="21">Semi-prefix</td>
    <td>第</td>
    <td>一 (one) → 第一 (first)</td>
  </tr>
  <tr align="center">
    <td>初</td>
    <td>一 (one) → 初一 (the first day of a lunar month)</td>
  </tr>
  <tr align="center">
    <td>十</td>
    <td>一 (one) → 十一 (eleven)</td>
  </tr>
  <tr align="center">
    <td>周</td>
    <td>一 (one) → 周一 (Monday)</td>
  </tr>
  <tr align="center">
    <td>星期</td>
    <td>一 (one) → 星期一 (Monday)</td>
  </tr>
  <tr align="center">
    <td>老</td>
    <td>虎 (tiger) → 老虎 (tiger)</td>
  </tr>
  <tr align="center">
    <td>小</td>
    <td>草 (grass) → 小草 (grass)</td>
  </tr>
  <tr align="center">
    <td>大</td>
    <td>海 (sea) → 大海 (large sea)</td>
  </tr>
  <tr align="center">
    <td>半</td>
    <td>导体 (conductor) → 半导体 (semiconductor)</td>
  </tr>
  <tr align="center">
    <td>单</td>
    <td>细胞 (cell) → 单细胞 (unicell)</td>
  </tr>
  <tr align="center">
    <td>超</td>
    <td>链接 (link) → 超链接 (hyperlink)</td>
  </tr>
  <tr align="center">
    <td>次</td>
    <td>大陆 (continent) → 次大陆 (subcontinent)</td>
  </tr>
  <tr align="center">
    <td>非</td>
    <td>常规 (conventional) → 非常规 (unconventional)</td>
  </tr>
  <tr align="center">
    <td>每</td>
    <td>次 (time) → 每次 (every time)</td>
  </tr>
  <tr align="center">
    <td>全</td>
    <td>明星 (star) → 全明星 (all star)</td>
  </tr>
  <tr align="center">
    <td>伪</td>
    <td>君子 (gentlemen) → 伪君子 (hypocrites)</td>
  </tr>
  <tr align="center">
    <td>亚</td>
    <td>热带 (tropical zone) → 亚热带 (sub-tropical zone)</td>
  </tr>
  <tr align="center">
    <td>洋</td>
    <td>酒 (wine) → 洋酒 (foreign wine)</td>
  </tr>
  <tr align="center">
    <td>总</td>
    <td>比分 (score) → 总比分 (total score)</td>
  </tr>
  <tr align="center">
    <td>反</td>
    <td>物质 (matter) → 反常规 (antimatter)</td>
  </tr>
  <tr align="center">
    <td>副</td>
    <td>总统 (president) → 副总统 (vice president)</td>
  </tr>

  <tr align="center">
    <td rowspan="41">Semi-suffix</td>
    <td>们</td>
    <td>我 (I) → 我们 (we)</td>
  </tr>
  <tr align="center">
    <td>里</td>
    <td>这 (here) → 这里 (here)</td>
  </tr>
  <tr align="center">
    <td>些</td>
    <td>这 (this) → 这些 (these)</td>
  </tr>
  <tr align="center">
    <td>样</td>
    <td>这 (this) → 这样 (such)</td>
  </tr>
  <tr align="center">
    <td>个</td>
    <td>这 (this) → 这个 (this one)</td>
  </tr>
  <tr align="center">
    <td>边</td>
    <td>这 (this) → 这边 (here)</td>
  </tr>
  <tr align="center">
    <td>种</td>
    <td>这 (this) → 这种 (this kind)</td>
  </tr>
  <tr align="center">
    <td>次</td>
    <td>这 (this) → 这次 (this time)</td>
  </tr>
  <tr align="center">
    <td>儿</td>
    <td>这 (this) → 这儿 (here)</td>
  </tr>
  <tr align="center">
    <td>部</td>
    <td>东 (east) → 东部 (east)</td>
  </tr>
  <tr align="center">
    <td>中</td>
    <td>心 (heart) → 心中 (in the heart)</td>
  </tr>
  <tr align="center">
    <td>上</td>
    <td>山 (mountain) → 山上 (on the mountain)</td>
  </tr>
  <tr align="center">
    <td>面</td>
    <td>前 (front) → 前面 (in the front)</td>
  </tr>
  <tr align="center">
    <td>者</td>
    <td>强 (strong) → 强者 (the strong one)</td>
  </tr>
  <tr align="center">
    <td>家</td>
    <td>科学 (science) → 科学家 (scientist)</td>
  </tr>
  <tr align="center">
    <td>子</td>
    <td>胖 (fat) → 胖子 (a fat man)</td>
  </tr>
  <tr align="center">
    <td>头</td>
    <td>木 (wood) → 木头 (wood)</td>
  </tr>
  <tr align="center">
    <td>工</td>
    <td>木 (wood) → 木工 (carpentry)</td>
  </tr>
  <tr align="center">
    <td>匠</td>
    <td>木 (wood) → 木匠 (carpenter)</td>
  </tr>
  <tr align="center">
    <td>星</td>
    <td>笑 (laugh) → 笑星 (comedian)</td>
  </tr>
  <tr align="center">
    <td>手</td>
    <td>老 (old) → 老手 (old hand)</td>
  </tr>
  <tr align="center">
    <td>主义</td>
    <td>乐观 (optimistic) → 乐观主义 (optimism)</td>
  </tr>
  <tr align="center">
    <td>鬼</td>
    <td>吝啬 (stingy) → 吝啬鬼 (miser)</td>
  </tr>
  <tr align="center">
    <td>式</td>
    <td>中 (Chinese) → 中式 (Chinese style)</td>
  </tr>
  <tr align="center">
    <td>队</td>
    <td>考古 (archaeology) → 考古队 (archaeological team)</td>
  </tr>
  <tr align="center">
    <td>色</td>
    <td>黄 (yellow) → 黄色 (the yellow color)</td>
  </tr>
  <tr align="center">
    <td>学</td>
    <td>地质 (geology) → 地质学 (discipline of geology)</td>
  </tr>
  <tr align="center">
    <td>论</td>
    <td>宿命 (fate) → 宿命论 (fatalism)</td>
  </tr>
  <tr align="center">
    <td>站</td>
    <td>汽车 (bus) → 汽车站 (bus station)</td>
  </tr>
  <tr align="center">
    <td>仪</td>
    <td>光谱 (spectrum) → 光谱仪 (spectrograph)</td>
  </tr>
  <tr align="center">
    <td>界</td>
    <td>学术 (academic) → 学术界 (academia)</td>
  </tr>
  <tr align="center">
    <td>族</td>
    <td>追星 (chasing a star) → 追星族 (fans)</td>
  </tr>
  <tr align="center">
    <td>棍</td>
    <td>赌 (gamble) → 赌棍 (gambler)</td>
  </tr>
  <tr align="center">
    <td>灾</td>
    <td>雨 (rain) → 雨灾 (rain disaster)</td>
  </tr>
  <tr align="center">
    <td>气</td>
    <td>冷 (cold) → 冷气 (cold air)</td>
  </tr>
  <tr align="center">
    <td>性</td>
    <td>酸 (acid) → 酸性 (acidic)</td>
  </tr>
  <tr align="center">
    <td>厅</td>
    <td>歌 (song) → 歌厅 (KTV)</td>
  </tr>
  <tr align="center">
    <td>机</td>
    <td>复印 (copy) → 复印机 (copier)</td>
  </tr>
  <tr align="center">
    <td>法</td>
    <td>说 (say) → 说法 (saying)</td>
  </tr>
  <tr align="center">
    <td>剧</td>
    <td>粤 (Yue) → 粤剧 (Cantonese Opera)</td>
  </tr>
  <tr align="center">
    <td>长</td>
    <td>船 (ship) → 船长 (captain of a ship)</td>
  </tr>
</table>

<table>
  <tr align="center">
    <td colspan="3"><b>Semantic Questions</b></td>
  </tr>
  <tr align="center">
    <td>Category</td>
    <td>Sub-category</td>
    <td>Example</td>
  </tr>
  <tr align="center">
    <td rowspan="9">Geography</td>
    <td>country - capital</td>
    <td>中国 (China) - 北京 (Beijing)</td>
  </tr>
  <tr align="center">
    <td>country - currency</td>
    <td>中国 (China) - 人民币 (Chinese yuan)</td>
  </tr>
  <tr align="center">
    <td>province - abbreviation</td>
    <td>广东 (Guangdong) - 粤 (Yue)</td>
  </tr>
  <tr align="center">
    <td>province - capital</td>
    <td>广东 (Guangdong) - 广州 (Guangzhou)</td>
  </tr>
  <tr align="center">
    <td>province - drama</td>
    <td>广东 (Guangdong) - 粤剧 (Cantonese Opera)</td>
  </tr>
  <tr align="center">
    <td>province - channel</td>
    <td>广东 (Guangdong) - 广东卫视 (Guangdong Satellite TV)</td>
  </tr>
  <tr align="center">
    <td>province - university</td>
    <td>浙江 (Zhejiang) - 浙江大学 (Zhejiang University)</td>
  </tr>
  <tr align="center">
    <td>city - university</td>
    <td>南京 (Nanjing) - 南京大学 (Nanjing University)</td>
  </tr>
  <tr align="center">
    <td>university - abbreviation</td>
    <td>师范大学 (Normal University) - 师大 (Normal University)</td>
  </tr>

  <tr align="center">
    <td rowspan="4">History</td>
    <td>dynasty - emperor</td>
    <td>汉 (Han) - 刘邦 (Liu Bang)</td>
  </tr>
  <tr align="center">
    <td>dynasty - capital</td>
    <td>秦 (Qin) - 咸阳 (Xian Yang)</td>
  </tr>
  <tr align="center">
    <td>title - emperor</td>
    <td>汉高祖 (Emperor Gaozu of Han) - 刘邦 (Liu Bang)</td>
  </tr>
  <tr align="center">
    <td>celebrity - country</td>
    <td>屈原 (Qu Yuan) - 楚国 (Country Chu)</td>
  </tr>

  <tr align="center">
    <td rowspan="10">Nature</td>
    <td>number</td>
    <td>第一 (first) - 状元 (the first in an imperial examination)</td>
  </tr>
  <tr align="center">
    <td>time</td>
    <td>春节 (Spring Festival) - 正月 (the first month in a lunar year)</td>
  </tr>
  <tr align="center">
    <td>animal</td>
    <td>公鸡 (cock) - 母鸡 (hen)</td>
  </tr>
  <tr align="center">
    <td>plant</td>
    <td>杏树 (apricot tree) - 杏 (apricot)</td>
  </tr>
  <tr align="center">
    <td>ornament</td>
    <td>手指 (finger) - 戒指 (ring)</td>
  </tr>
  <tr align="center">
    <td>chemistry</td>
    <td>盐 (salt) - 氯化钠 (sodium chloride)</td>
  </tr>
  <tr align="center">
    <td>physics</td>
    <td>冰 (ice) - 水蒸气 (steam)</td>
  </tr>
  <tr align="center">
    <td>weather</td>
    <td>小满 (Grain Full) - 夏天 (summer)</td>
  </tr>
  <tr align="center">
    <td>reverse</td>
    <td>松 (loose) - 紧 (tight)</td>
  </tr>
  <tr align="center">
    <td>color</td>
    <td>海 (sea) - 蓝色 (blue)</td>
  </tr>

  <tr align="center">
    <td rowspan="5">People</td>
    <td>company - founder</td>
    <td>阿里巴巴 (Alibaba) - 马云 (Ma Yun)</td>
  </tr>
  <tr align="center">
    <td>work - scientist</td>
    <td>地动仪 (seismograph) - 张衡 (Zhang Heng)</td>
  </tr>
  <tr align="center">
    <td>work - writer</td>
    <td>朝花夕拾 (Dawn Blossoms Plucked at Dusk) - 鲁迅 (Lu Xun)</td>
  </tr>
  <tr align="center">
    <td>family - member</td>
    <td>爷爷 (grandfather) - 孙子 (grandson)</td>
  </tr>
  <tr align="center">
    <td>student - degree</td>
    <td>小学 (elementary school) - 小学生 (schoolchild)</td>
  </tr>
</table>

##  <a name="reference"></a>Reference
Shen Li, Zhe Zhao, Renfen Hu, Wensi Li, Tao Liu, Xiaoyong Du, <em>Analogical Reasoning on Chinese Morphological and Semantic Relations</em>, ACL 2018.

Xinxiong Chen, Lei Xu, Zhiyuan Liu, Maosong Sun, and Huanbo Luan. 2015. Joint learning of character and word embeddings. In IJCAI. pages 1236–1242.

Yuehua Liu, Wenyu Pan, and Wei Gu. 2001. Practical grammar of modern Chinese. The Commercial Press.
