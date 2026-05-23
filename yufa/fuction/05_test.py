"""
    函数综合案例
"""
money = 5000000
name = input("请输入您的姓名:")
def show_money():
    print(f"{name}您好,余额为{money}")
def save_money():
    global money
    money += float(input("请输入要存的金额:"))
    print(f"余额为{money}")
def take_money():
    global money
    f = float(input("请输入取款金额:"))
    if(money >= f):
     money -= f
     print(f"取款成功,余额为{money}")
    else:
     print("余额不足")
def show_menu():
    num = int(input((f"""
    {name}您好
    请输入要办理的业务代号
    1.查询余额
    2.存款
    3.取款
    4.退出
    """)))
    if(num == 1):
        show_money()
    elif(num == 2):
        save_money()
    elif(num == 3):
        take_money()
    else:
        global b
        b = False
b = True
while(b):
    show_menu()