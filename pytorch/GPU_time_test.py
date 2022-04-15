'''
@Project: 三哥导师专利爬取.py   #项目名称
@Description:               #描述
@Time:2022-04-15 17:41       #日期
@Author:MING                #创建人
'''
import torch
import time

###CPU
start_time = time.time()
a = torch.ones(4000,4000)
for _ in range(10000):
    a += a
elapsed_time = time.time() - start_time

print('CPU time = ',elapsed_time)

###GPU
start_time = time.time()
b = torch.ones(4000,4000).cuda()
for _ in range(10000):
    b += b
elapsed_time = time.time() - start_time

print('GPU time = ',elapsed_time)