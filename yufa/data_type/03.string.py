"""
`   字符串数据类型的入门案例
"""
# my_str = "黑马程序员"
# for i in my_str:
#     print(i)
# i = 0
# while i < len(my_str):
#     print(my_str[i])
#     i+=1
my_str = "itheima itcast boxuegu"
print(my_str.count("it"))
my_str = my_str.replace(" ", "|")
print(my_str)
split = my_str.split("|")
print( split)
