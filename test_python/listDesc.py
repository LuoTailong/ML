# -*- coding: utf-8 -*-

# 通过列表表达式将符合条件的列表进行筛选
l1 = [x * x for x in range(10) if x > 3]
print(l1)
# 等价公式
result = []
for x in range(10):
    if x > 3:
        result.append(x * x)
        print(result)

# map函数--将函数作用于list
l = [1, 2, 3, 4]
print(type(l))
print(list(map(str, l)))

# Demo2:
freshFruit = ['banana', 'loganberry', 'passion fruit']
aList3 = []
for item in freshFruit:
    aList3.append(item.strip())
print(aList3)
# 等同于
aList5 = list(map(str.strip, freshFruit))
print(aList5)

