"""
    面向对象创建类
"""
class stu:
    name = None
    age = 0
    def __init__(self):
        self.name = "张三"
        self.age = 18
        print("初始化")
    def show(self):
        import winsound
        winsound.Beep(500,500)
    def __str__(self):
        return "name:%s,age:%d"%(self.name,self.age)
stu = stu()
print(stu)
