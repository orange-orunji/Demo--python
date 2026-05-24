"""
但是多种传参形式
"""
# 位置参数 - 默认使用形式
def func1(x,y):
    print(x,y)
func1(1,2)
# 关键字参数
def func2(name,age):
    print(name,age)
func2(age=18,name="wangwei")
# 缺省参数(默认值)
def fuc3(name,age,gender="男"):
    print(name,age,gender)
fuc3(age=18, name="wangwei")
fuc3( "王五",age=18)
# 不定长- 位置不定长,*号
def func4(*args):
    print(args)
func4(6,5,3,2,5,7,8,4,2)
# 不定长 - 关键字不定长,**号
def func5(**kwargs):
    print(kwargs)
func5(name="1234",age=18)
