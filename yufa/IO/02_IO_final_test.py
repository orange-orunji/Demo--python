"""
    综合案例
"""
r = open("D:\\a_develop\\py_imformation\\bill.txt", "r", encoding="UTF-8")
a = open("D:\\a_develop\\py_imformation\\bill.txt.bak","a",encoding="UTF-8")
for i in r:
    i = i.strip()
    if i.split(",")[4] == "测试":
        continue
    a.write(f"{i}\n")
a.close()
r.close()