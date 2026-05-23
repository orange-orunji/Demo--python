"""
    列表入门案例练习
"""
# # 定义这个列表,并用变量接收它
# stu_age_list = [21,25,21,23,22,20]
# print(stu_age_list)
# # 2.追加一个数字31，到列表的尾部
# stu_age_list.append(31)
# print(stu_age_list)
# # 3.追加一个新列表[29,33,30]到列表的尾部
# new_list = [29,33,30]
# stu_age_list.extend(new_list)
# # 4.去除第一个元素（应是21）
# stu_age_list.pop(0)
# print(stu_age_list)
# # 5.取出最后一个元素（应是30）
# pop = stu_age_list.pop()
# print(pop)
# print(stu_age_list)
# # 6.查找元素31，再列表中的下标位置
# print(stu_age_list.index(31))
# print(stu_age_list)
num_list = [1,2,3,4,5,6,7,8,9,10]
# for循环遍历取出里面的偶数并组成新的数组
new_list = []
for i in num_list:
    if i%2 == 0:
        new_list.append(i)
print(f"{num_list}-------------{new_list}")
new_list.clear()
i = 0
while i < len(num_list):
    if num_list[i]%2 == 0:
        new_list.append(num_list[i])
    i+=1
print(f"{num_list}-------------{new_list}")

