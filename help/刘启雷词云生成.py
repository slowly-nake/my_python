# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:07:25 2022

@author: 慢慢的蜗牛
"""

import wordcloud
import jieba
import matplotlib.pyplot as plt
# %%

with open('./比亚迪.txt', 'r', encoding='utf-8') as fp:
    news = fp.read()
# %%
stop_words = [line.strip() for line in open('stopwords.txt','r', encoding='utf-8').readlines()] + ['年', '月', '日']
#stop_words = []
news = news+ '知识搜索'*25+ '交互'*20
new = ' '.join(jieba.lcut(news))
# %%
ciyun = wordcloud.WordCloud(font_path='msyh.ttc',       # 中文
    background_color='white',    # 设置背景颜色为白色
    stopwords=stop_words)       # 设置禁用词，在生成的词云中不会出现set集合中的词
ciyun.generate(new)

plt.imshow(ciyun)
plt.show()
