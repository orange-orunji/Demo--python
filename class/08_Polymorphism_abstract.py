"""
    多态和抽象类的练习案例
"""
class Animal:
    def eat(self):
        pass
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class cat(Animal):
    def eat(self):
        print("猫吃鱼")
def func(obj):
    obj.eat()


dog = Dog()
c = cat()
func(dog)
func(c)

"""
    抽象类的练习
"""
class Air:
    def Refrigeration(self):
        pass
    def Sweeping_the_wind(self):
        pass
    def open(self):
        pass
class medieal_air(Air):
    def Refrigeration(self):
        print("美的空调")
    def Sweeping_the_wind(self):
        print("美的骚风")
    def open(self):
        print("美的打开")
class gelear_air(Air):
    def Refrigeration(self):
        print("格力空调")
    def Sweeping_the_wind(self):
        print("格力骚风")
    def open(self):
        print("格力打开")
def make_cold(air):
    air.Refrigeration()


medieal = medieal_air()
gelear = gelear_air()
make_cold(medieal)
make_cold(gelear)
