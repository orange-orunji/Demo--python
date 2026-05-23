"""
    元组的基本操作
"""

t1 = ('蔡徐坤',29,['basketball','music'])
print(t1.index(29))
print(t1[0])
del t1[2][0]
print(t1)
t1[2].append('coding')
print(t1)