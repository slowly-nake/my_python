'''
@Project: mysql_test.py   #项目名称
@Description:               #描述
@Time:2022-04-07 13:46       #日期
@Author:MING                #创建人
'''


import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='950102', charset='utf8')
cursor = conn.cursor()
cursor.execute('drop database first')
conn.commit()
cursor.execute('create database first DEFAULT CHARSET utf8 COLLATE utf8_general_ci')
conn.commit()
cursor.execute('show databases')
result = cursor.fetchall()
print(result)


cursor.close()
conn.close()
