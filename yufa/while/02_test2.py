"""
    while实现猜数字
"""
import random
num = random.randint(1, 100)
count = 0
b = True
while b :
    inputes = int(input("请输入要猜数字："))
    count += 1
    if(inputes == num):
        b = False
        print("恭喜你猜对了")
    else:
        if inputes > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")
print(f"次数是:{count}")