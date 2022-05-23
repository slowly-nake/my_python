# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:00:32 2022

@author: 慢慢的蜗牛
"""


def name(n):
    n = int(n)
    tem1 = str(2000 + n)
    tem2 = str(2004 + n)
    return r'./' + tem1 + '-' + tem2 + '.xlsx'

def read_film(n):
    df = pd.read_excel(n)
    df = df.set_index(df['Unnamed: 0']).drop(columns = 'Unnamed: 0')
    return df
# %%
import pandas as pd
import numpy as np
# %%

data = pd.read_excel('./省数据网络识别.xlsx')

# %%
for i in range(3,len(data)):
    n = data.loc[i].dropna()[0]
    nam1 = name(n)
    nam2 = data.loc[i].dropna()[1]
    nam2 = r'./new/' + str(nam2) + '.xlsx'
    df = read_film(nam1)
    li = data.loc[i].dropna()[2:]
    df.loc[li, li].to_excel(nam2)
    
                
    

