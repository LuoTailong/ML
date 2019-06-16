# -*- coding: utf-8 -*-

# 惰性求值
t1 = (x * x for x in range(10))
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(list(t1))
print(list(t1))
print(list(t1))

# python中将多元素复制叫做序列解包
a, b = 1, 1
print(a, b)
(x, y, z) = 1, 2, 3
print(x, y, z)
