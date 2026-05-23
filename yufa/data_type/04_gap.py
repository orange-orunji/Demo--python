"""
    切片入门案例
"""
my_str = "万过薪月,员序程马黑来,nohtyP学"
print(my_str[9:4:-1])

split = my_str[::-1].split(",")
print(split[1].replace("来",""))
