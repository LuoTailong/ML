# -*- coding: utf-8 -*-

f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

print((lambda x, y: x * y)(1, 2))


# 等价于
def mul(x, y):
    return x * y


res1 = mul(1, 2)
print(res1)

print(list(map(lambda x, y: x * y, range(10), range(10))))
