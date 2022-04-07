# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:21:05 2022

@author: 慢慢的蜗牛
"""
import requests
import pandas as pd
from lxml import etree

# %%
'''
url = 'https://tax.tianyancha.com/2966635808?tabnav=base'
headers = {
            'Cookie': 'aliyungf_tc=d170b85e8116fd0f334fc11c98e3648fa8247103b5acb919d82b18d83bf08e0f; csrfToken=SMtabXjMjuE5bVWOpPEXyLjh; jsid=SEO-BAIDU-ALL-SY-000001; TYCID=b394cb20b0cd11ecbda3ff15025345b4; ssuid=3234061856; sajssdk_2015_cross_new_user=1; bannerFlag=true; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2218052258813%22}; tyc-user-info-save-time=1648715930988; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA1MjI1ODgxMyIsImlhdCI6MTY0ODcxNTkzMCwiZXhwIjoxNjUxMzA3OTMwfQ.YM66WX2MGu8iA96QIaRP5Yu2HhX22a6TA325sOWCj-adnp2RP6FwoZAObz5I_LDwd8JJ06MY-KYmKbOyOk9PKw; tyc-user-phone=%255B%252218052258813%2522%255D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22211624248%22%2C%22first_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%7D',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
           }
requ = requests.get(url=url, headers=headers)
'''


# %%
data = pd.read_excel(r'C:\Users\慢慢的蜗牛\Desktop\打工是不可能打工的\高新区工作文件\整理名单(完成).xlsx')


# %%
headers = {
'Cookie': 'aliyungf_tc=d170b85e8116fd0f334fc11c98e3648fa8247103b5acb919d82b18d83bf08e0f; csrfToken=SMtabXjMjuE5bVWOpPEXyLjh; TYCID=b394cb20b0cd11ecbda3ff15025345b4; ssuid=3234061856; sajssdk_2015_cross_new_user=1; bannerFlag=true; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2218052258813%22}; tyc-user-info-save-time=1648715930988; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA1MjI1ODgxMyIsImlhdCI6MTY0ODcxNTkzMCwiZXhwIjoxNjUxMzA3OTMwfQ.YM66WX2MGu8iA96QIaRP5Yu2HhX22a6TA325sOWCj-adnp2RP6FwoZAObz5I_LDwd8JJ06MY-KYmKbOyOk9PKw; tyc-user-phone=%255B%252218052258813%2522%255D; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-BIAOTI; searchSessionId=1648719605.63186851; CT_TYCID=88fc4a7ee6414c86889bc4f54a7097a4; RTYCID=acad208cb2a543c590d4bfa4e74b8e0d; cloud_token=38e6105363a14f94960b599294965e23; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22211624248%22%2C%22first_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%7D',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
params = {'tabnav': 'base'}
for i in range(len(data)):
    url = 'https://tax.tianyancha.com/search/' + data['单位名称'][i]
    #print(url)
    requ_up = requests.get(url=url, headers=headers)
    page_out = etree.HTML(requ_up.text)
    try:    
        url_in = page_out.xpath('//*[@id="search"]/div[2]/div[1]/div[2]/a/@href')[0]
        #print(url_in)
        requ_in = requests.get(url=url_in, headers=headers, params=params)
        page_in = etree.HTML(requ_in.text)
        data['法人'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div/div[1]/div[2]/div[1]/a/text()')[0]
        data['注册资本'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]/div/text()')[0]
        data['实缴资本'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[4]/text()')[0]
        data['成立日期'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]/div/text()')[0]
        data['社会统一信用代码'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[2]/text()')[0]
        data['工商注册号'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[4]/text()')[0]
        data['企业电话'][i] = page_in.xpath('//*[@id="web-content"]/div/div[1]/div[1]/div[2]/div[3]/div/text()')[0]
        data['企业经营地址'][i] = page_in.xpath('//*[@id="web-content"]/div/div[1]/div[1]/div[2]/div[4]/div/span/text()')[0]
        data['开户银行'][i] = page_in.xpath('//*[@id="web-content"]/div/div[1]/div[1]/div[2]/div[5]/div/span/text()')[0]
        data['银行账户'][i] = page_in.xpath('//*[@id="web-content"]/div/div[1]/div[1]/div[2]/div[6]/div/span/text()')[0]
        data['经营状态'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[4]/text()')[0]
        data['注册地址'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[10]/td[2]/text()')[0]
        data['参保人数'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[8]/td[4]/text()')[0]
        data['人员规模'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[8]/td[2]/text()')[0]
        data['纳税人资质'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[4]/text()')[0]
        data['所属行业'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]/text()')[0]
        data['经营范围'][i] = page_in.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[11]/td[2]/span/text()')[0]
        
        num = (i / len(data)) * 100
        print(str(num)+'%')
    except:
        print(i)


# %%

data.to_excel(r'C:\Users\慢慢的蜗牛\Desktop\打工是不可能打工的\高新区工作文件\整理名单(完成).xlsx')
    

# %%
'''
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'TYCID=b394cb20b0cd11ecbda3ff15025345b4; ssuid=3234061856; sajssdk_2015_cross_new_user=1; aliyungf_tc=29988b8d56e4c38f85cfe94f2a872e3b1a4d3e8db96ebd07c2bc315c38cf631c; csrfToken=piKJ71r7dPQC0RM5K2BI8Y-R; _bl_uid=pRlXy1s2eeqqCqvyFkXyxk6iz9vz; bannerFlag=true; tyc-user-info-save-time=1648715930988; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA1MjI1ODgxMyIsImlhdCI6MTY0ODcxNTkzMCwiZXhwIjoxNjUxMzA3OTMwfQ.YM66WX2MGu8iA96QIaRP5Yu2HhX22a6TA325sOWCj-adnp2RP6FwoZAObz5I_LDwd8JJ06MY-KYmKbOyOk9PKw; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2218052258813%22}; tyc-user-phone=%255B%252218052258813%2522%255D; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-BIAOTI; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22211624248%22%2C%22first_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E5%A4%A9%E7%9C%BC%E6%9F%A5%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%7D%2C%22%24device_id%22%3A%2217fdf1ec9a0bfd-01ed8583cd369d-56171958-1338645-17fdf1ec9a1f66%22%7D; bdHomeCount=0; searchSessionId=1648719605.63186851; creditGuide=1; CT_TYCID=88fc4a7ee6414c86889bc4f54a7097a4; cloud_token=205364887d944dcf98cc33cdde01ca00; cloud_utm=5ab673c2661a471f8d21c117a84826b6; RTYCID=acad208cb2a543c590d4bfa4e74b8e0d; acw_tc=2f6fc12c16487197754938676e21c47db9fde4b9b72ddc81987822063b0de4',
    'Host': 'www.tianyancha.com',
    'Referer': 'https://www.tianyancha.com/vipintro?itchpointflag=pc_home_vipbutton',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    U'pgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
url = 'https://www.tianyancha.com/search'
for i in data:
    params = {
        'key': '西安世科电子科技有限公司'
        }
    requ = requests.get(url=url, headers=headers, params=params).text
    ''' 