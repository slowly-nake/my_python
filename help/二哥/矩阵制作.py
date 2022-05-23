# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:58:58 2022

@author: 慢慢的蜗牛
"""
import numpy as np
import pandas as pd
# %%
data = pd.read_excel('./省数据时间窗.xlsx')

# %%

data = data.fillna(1001)
c = '2006-2010'
# %%
tem_1 = np.full((347, 347), 0)


# %%
for i in data[c]:
    i = str(i)
    li = i.split(';')
    for j in li:
        j = int(j) - 1001
        for x in li:
            x = int(x) - 1001
            if x==j:
                tem_1[j, x] = 0
            else:
                tem_1[j, x] = 1

# %%
a = [i + 1000 for i in range(1, 348)]
df = pd.DataFrame(data = tem_1, index=a, columns=a)

# %%
save = df.loc[df.sum(axis=1) != 0, df.sum(axis=0) != 0]


# %%
save.to_excel('./%s.xlsx'%c)