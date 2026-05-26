"""
    数据库连接练习
"""
from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Fjw200511071"
)
conn.select_db("hmdp")
# 获取游标对象
cursor = conn.cursor()

# 通过浮标对象来对数据库进行操作
cursor.execute("select * from tb_blog")
print(cursor.fetchall())
cursor.close()
conn.close()