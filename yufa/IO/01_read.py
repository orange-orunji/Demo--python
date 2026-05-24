"""
    IO流中的读写操作
"""
# 打开文件(获取操作文件对象)
# f = open("D:\\a_develop\\py_imformation\\ioTest1.txt", "r", encoding="UTF-8")
# 读取文件-read()
# print(f.read(1024))
# 读取文件-readLines()
# print(f.readlines())
# 读取文件 - readline()
# print(f.readline())
# for循环读取文件行
# for i in f:
#     print(i)
# 文件的关闭
# f.close()
# with open 突发操作文件
# with open("D:\\a_develop\\py_imformation\\ioTest1.txt", "r", encoding="UTF-8") as f:
#     print(f.read())
# 练习
count = 0
# with open("D:\\a_develop\\py_imformation\\ioTest1.txt", "r", encoding="UTF-8") as f:
#     for i in f:
#         count += i.count("itheima")
with open("D:\\a_develop\\py_imformation\\ioTest1.txt", "r", encoding="UTF-8") as f:
    for i in f:
        list = i.strip("\n").split(" ")
        for j in list:
            if(j == "itheima"):
                count += 1
print( count)