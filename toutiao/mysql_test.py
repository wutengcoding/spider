#coding=utf-8
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("39.107.117.64","root","123456","mysql" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SHOW TABLES;")
# cursor.execute("select * from tables_priv limit 10;")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
data = cursor.fetchall()

for d in data:
    print(d)
# print ('\n'.join(data))

# 关闭数据库连接
db.close()