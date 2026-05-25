"""
    class类的定义和使用
"""
class student:
    name = None
    gender = None
    age = None
    score = None
    def hello(self):
        print(f"hello,my name is{self.name}" )
    def hello1(self,msg):
        print(f"hello,my name is{self.name},{msg}" )
stu = student()
stu.name = "张三"
stu.gender = "男"
stu.hello1("你们这群傻叼")