# -*- coding: utf-8 -*-

# set--集合 无序 唯一
set1 = {1, 2, 3, 4, 5}
set2 = set(range(10))
set3 = set([1, 2, 3, 4])
set4 = set((1, 2, 3, 4))
set5 = set({"Apple": 1, "pear": 2})
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)

# 集合增加元素
set1.add(100)
print(set1)
# 集合删除元素
set1.remove(100)
# 集合的更新操作
set1.update({100, 200, 300})
# 集合运算--交并补
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 2}
# 补集
print(s1 - s2)
print(s1.difference(s2))
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)
print(s1.union(s2))
# 包含
print(s3 < s1)
print(s3 < s2)
# 去重
l1 = [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6]
print(set(l1))