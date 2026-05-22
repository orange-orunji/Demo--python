"""
    while案例实现九九乘法表
"""
i = 1
while i <= 9 :
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}",end="\t")
        j+=1
    i+=1
    print()