"""
    循环嵌套练习
"""
i = 0
while i <= 100:
    print(f"今天是第{i}天告白")
    j = 0
    while j <= 10:
        print(f"今天是第{i}天第{j}朵花")
        j+=1
    print("依依我喜欢你")
    i +=1
print(f"{i-1}天告白结束")
