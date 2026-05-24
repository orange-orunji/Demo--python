"""
异常捕获练习
"""
try:
    a = int(input("请输入数字:"))
    b = int(input("请输入数字:"))
    print(a/b)
    print(name)
except Exception as e:
    print(e)