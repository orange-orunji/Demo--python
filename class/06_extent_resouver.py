"""
    覆写
"""
class Phone:
    name = "phone"
    def call(self):
        print(f"{self.name}正在通话中")
class phone(Phone):
    name = "子类"
    def call(self):
        print(f"{self.name}正在通话中")
        print(f"{Phone.name}正在通话中")
p = phone()
p.call()
