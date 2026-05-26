"""
    定义返回的数据类型
"""
class Resource():
    def __init__(self,date,orders,income,adress):
        self.date = date
        self.orders = orders
        self.income = income
        self.adress = adress
    def __str__(self):
        return "{} {} {} {}".format(self.date,self.orders,self.income,self.adress)