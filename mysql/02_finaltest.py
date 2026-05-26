"""
    将文件读取内容写入数据库
"""
from pymysql import Connection
from fileRead.data_define import Resource
from fileRead.file_define import file_reader,file_JSON_reader
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Fjw200511071",
    autocommit=True
)
conn.select_db("teach")
cursor = conn.cursor()
r = file_reader().data_read("D:/a_develop/py_imformation/file1.txt")
rj = file_JSON_reader().data_read("D:/a_develop/py_imformation/fileJSON.txt")
l: list[Resource] = r + rj
for i in l:
    cursor.execute("insert into orders(order_date,order_id,money,province) values(%s,%s,%s,%s)",(i.date,i.orders,i.income,i.adress))
