# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:22:46 2021

@author: 慢慢的蜗牛
"""

from selenium import webdriver
# %%

import time
import random
# %%
web = webdriver.Edge()


# %%
web.get('https://www.douyu.com/topic/CFHDZBDKS?rid=3481256')

# %%


text = web.find_element_by_css_selector('#layout-Player-aside > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea')
text.send_keys('这是个善意的测试机器人')

bottom = web.find_element('xpath', '//*[@id="layout-Player-aside"]/div[2]/div/div[2]/div[3]/div[2]')



# %%
#li = ['欢哥早啊', '欢哥真帅', '666', '卧槽牛啊', '老六', '什么魔鬼', '啊,,,这']
li = ['富强','民主','文明','和谐','自由','平等','公正','法治','爱国','敬业','诚信','友善']
#li = ['直播间里有活人么？', '我不刷了', '大家出来聊聊天啊', '没有活人了么', '那我先走了', '我过一会再来']
while 1:
    #text = web.find_element_by_css_selector('#layout-Player-aside > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea')
    for i in range(12):
        text.send_keys(li[i])
        #text.send_keys('主播说他不是gay，喜欢主播的大家点个免费的关注呀，谢谢大家！')
        time.sleep(5)
        bottom.click()
    time.sleep(60)