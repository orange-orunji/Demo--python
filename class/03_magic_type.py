"""
    类中的魔术方法
"""
class student:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name: %s, age: %s" % (self.name, self.age)
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age >= other.age
    def __eq__(self, other):
        return self.age == other.age

sut = student("张三",18)
sut1 = student("lisis",20)
sut2 = student("wangwu",20)
print(sut)
print(sut<sut1)
print(sut<=sut2)
print(sut==sut2)