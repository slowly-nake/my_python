# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:17:09 2022

@author: 慢慢的蜗牛
"""
import requests
import pandas as pd
from lxml import etree
# %%
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection': 'keep-alive',
'Host': 'www.zhonghongwang.com',
'Referer': r'https://www.zhonghongwang.com/index.php?f=search&searchsousuo=%E5%8D%8E%E4%B8%BA&page=1',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform':'"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1'
    
    }

url = 'https://www.zhonghongwang.com/index.php?f=search&searchsousuo=%E5%8D%8E%E4%B8%BA'

# %%
b = []
for i in range(1,2):
    params = {
    'f': 'search',
    'searchsousuo': '比亚迪',
    'page': i
    }

    resu = requests.get(url=url, headers=headers, params=params).text
    result = etree.HTML(resu)
    a = result.xpath('/html/body/div[4]/div[1]/ul/li/a/@href')
    b += a
    print(a)
# %%
with open(r'D:\python file\my github\my_python\help\比亚迪.txt', 'w', encoding='utf-8') as fp:
    for i in b:
        urlin = 'https://www.zhonghongwang.com' + i
        ret = requests.get(url=urlin, headers=headers).text
        result = etree.HTML(ret)
        a = result.xpath('/html/body/div[2]/div[2]/div[1]/p//text()')
        for j in a:
            if j not in ['以上内容为本网站转自其它媒体，相关信息仅为传递更多信息之目的，不代表本网观点，亦不代表本网站赞同其观点或证实其内容的真实性。如稿件版权单位或个人不想在本网发布，可与本网联系，本网视情况可立即将其撤除。\n' , '免责声明：' , '\n    ' , '\n    .mzsm{\n        font-size: 16px;\n        line-height: 26px;\n        color: #555;\n        word-wrap: break-word;\n        text-align: justify;\n        padding: 13px 0; \n        margin-top: 30px;\n    }\n',
 '\n' , '\n                                        ']:
                fp.write(j)
                print(j)