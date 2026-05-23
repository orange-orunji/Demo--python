"""
    函数的定义
"""
def my_len(s):
    count = 0
    for i in s:
        count += 1
    return  count
print(my_len("hello world"))