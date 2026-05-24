"""
演示函数作为参数传递
"""
# 定义一个函数,接收另一个函数作为传入参数
def fuct_1(commond):
    result = commond(1,2)
    print(result)
# 定义一个函数准备作为参数传入另一个参数
def add(a,b):
    return a+b
# 调用,并传入函数
fuct_1(add)