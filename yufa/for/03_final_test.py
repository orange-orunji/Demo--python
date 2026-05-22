"""
    综合案例
"""
import random
all = 10000
# while all > 0:
for i in range(1,21):
        print("余额为：", all)
        r = random.randint(1, 10)
        if  r <=5 :
            print(f"员工{i}绩点未达标,绩点为{r}")
            continue
        else:
            if all >= 1000:
                all -= 1000
                print(f"员工{i}绩点达标,绩点为{r},领取奖金1000元,剩余余额为{all}元")
            else:
                break
