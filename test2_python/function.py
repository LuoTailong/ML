# -*- coding: utf-8 -*-
def SayHello():
    print("哈喽 " * 5)


def RepeationStr(str):
    print("[" + str + "]")


def SayHi():
    return "你好 " * 5


def AddThreeNumber(a, b, c):
    return a + b + c


if __name__ == '__main__':
    SayHello()
    SayHello()
    RepeationStr("哈哈")
    result = SayHi()
    print(result)
    result1 = AddThreeNumber(1, 2, 3)
    print("Three Number sum result is :{}".format(result1))
