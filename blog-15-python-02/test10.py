# -*- coding: utf-8 -*-
import MySQLdb

#建立连接
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456'
    )

#执行最简单的语句
cus = conn.cursor()

#查看MySQL的版本
sql = 'select version()'

cus.execute(sql)

#查看返回结果
print(cus.fetchone())

#关闭连接和对象
cus.close()
conn.close()
