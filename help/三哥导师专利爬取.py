# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:45:57 2022

@author: 慢慢的蜗牛
"""

import pandas as pd
import requests

# %%
code_data = pd.read_excel(r'./上市公司绿色专利申请情况(1).xlsx', dtype=object)

# %%

temp = pd.DataFrame(columns=['code', 'codee', 'industry', 'subdivide'])
li = list(set(code_data['Scode']))
temp.code = [str(i) for i in li]


#%%
for i in range(len(temp.code)):
    if int(temp.code[i]) <= 310000:
        temp.codee[i] = 'sz' + temp.code[i]
    else:
        temp.codee[i] = 'sh' + temp.code[i]


# %%

url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/CompanySurveyAjax?'
headers = {
    'Connection': 'close',
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'    }

for i in range(len(temp)):
    params = {
        'type': 'web',
            'code': temp.codee[i]
            }
    results = requests.get(url=url,headers=headers, params=params).json()
    indt = results['jbzl']['sszjhhy'].split('-')
    temp.industry[i] = indt[0]
    temp.subdivide[i] = indt[1]
    p = (i/len(temp))*100
    p = str(p) + '%'
    print(p)


    # %%
new = temp.set_index(temp.code)
new = new.drop(['code', 'codee'], axis=1)
dr = new.to_dict()

    # %%
li = list(code_data.Scode)
code_data.Scode = [str(i) for i in li]

    # %%
code_data['industry'] = ''
code_data['subdivide'] = ''

    # %%
for i in range(len(code_data)):
    code_data.industry[i] = dr['industry'][code_data.Scode[i]]
    code_data.subdivide[i] = dr['subdivide'][code_data.Scode[i]]

    # %%
code_data.to_excel(r'./finish_申请（新）.xlsx')