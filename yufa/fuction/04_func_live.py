"""
    函数的生命周期和修改全局变量galbol
"""
num = 200
def fun_a():
    print(num)
def fun_b():
    global num
    num = 300
    print(num)
fun_a()
fun_b()