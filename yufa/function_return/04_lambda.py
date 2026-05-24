"""
    演示lambda匿名函数
"""
# 定义一个函数.接收奇谭函数输入
def fuc1(compute):
    print(compute(1,2))
# 通过lambda你们函数的形式,将你们函数作为参数传入
fuc1(lambda  x,y:x+y)