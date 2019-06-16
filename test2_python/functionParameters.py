# -*- coding: utf-8 -*-
# 默认参数
def SayHello(str="ssss", time=10):
    return str * time


# 关键字参数
def AddThreeNumber(a, b, c):
    print(a + b + c)


# VarArgs参数
# * 表示可迭代的对象 如元组
# ** 表示字典 key--value
vec = [[1, 2], [3, 4], [5, 6]]
print(list(map(list, zip(*vec))))
print(list(map(list, zip([1, 2], [3, 4], [5, 6]))))


def printFunction(fparameters, *tuple1, **dict1):
    print(fparameters)
    print(tuple1)
    print(dict1)


if __name__ == '__main__':
    re1 = SayHello("HelloWorld")
    print(re1)
    AddThreeNumber(1, 2, 3)
    AddThreeNumber(c=1, b=2, a=3)
    AddThreeNumber(a=1, b=2, c=3)
    printFunction(1, 2, 3, "apple", name="hangSan", age=10)
