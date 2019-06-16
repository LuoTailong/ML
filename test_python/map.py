# -*- coding: utf-8 -*-

# way1
print(list(map(str, range(3))))


# way2
def add1(x):
    return x + 5


r1 = list(map(add1, range(10)))
print(r1)


# way3
def add2(x, y):
    return x + y


r2 = list(map(add2, range(5), range(5)))
print(r2)

# 等同于
print(list(map(lambda x, y: x + y, range(5), range(5, 10))))
print([add2(x, y) for x, y in zip(range(5), range(5, 10))])

# 导入reduce函数
from functools import reduce

print(reduce(add2, range(5)))
print(reduce(lambda x, y: x + y, range(5)))

seq1 = ['foo', 'x41', '?1', '***']


def func(x):
    return x.isalnum()


filter(func, seq1)
print(list(filter(func, seq1)))

# 使用列表推导式实现相同的功能
print([x for x in seq1 if x.isalnum()])
