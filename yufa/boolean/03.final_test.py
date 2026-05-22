import random

target = random.randint(1,10);

if (num := int(input("请输入第一次猜想的数字:"))) != target:
    if num<target:
        print("你猜的数字小了")
    else:
        print("你猜的数字大了")
    if (num := int(input("不对,再猜一次:"))) != target:
        if num < target:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")
        if (num := int(input("不对,最后猜一次:"))) != target:
            print(f"你猜的数字不对哦正确答案是:{target}")
        else:
            print("你猜的数字正确")
    else:
        print("你猜的数字正确")
else:
    print("你猜的数字正确")