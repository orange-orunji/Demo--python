"""
    演示python中的if判断语句
"""
import random
age = 30
if age >= 18:
    print("你已成年可投票")
    print("时间过得真快啊")
print("------------------------------------------------------")
#
# if int(input("""
#     欢迎来到黑马儿童游乐园,儿童免费,成人收费
#     请输入你的年龄：""")) <=18:
#     print("您还没有成年,免票")
# elif int(input("请输入宁的身高:")) <=120:
#     print("您的身高未超出120cm,可以免费游玩")
# elif int(input("请告诉我今天是星期几:")) == 1:
#     print("今日是星期一,免费")
# else:
#     print("您已成年,游玩需要补票10元")
# print("祝您游玩愉快")
target = random.randint(1,10);
if int(input("请输入第一次猜想的数字")) == target:
    print("恭喜你猜对了")
elif int(input("不对,再猜一次:")) == target:
    print("感谢你猜对了")
elif int(input("不对,最后猜一次:")) == target:
    print("感谢你猜对了")
else:
    print(f"你猜的数字都猜不对了,下次加油,我想的是:{target}")