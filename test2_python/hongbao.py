# -*- coding: utf-8 -*-
import random


def hongBao(total, num):
    # total:指红包有多少钱
    # num:指红包有多少个
    each = []  # 存放发放的明细
    already = 0  # 存放给前n-1个人发放的金额
    for i in range(1, num):
        t = random.randint(1, (total - already) - (num - i))
        already += t
        each.append(t)
    each.append(total - already)
    return each


if __name__ == '__main__':
    total = int(input("please input your total number:"))
    num = int(input("please input your num:"))
    for i in range(30):
        result = hongBao(total, num)
        print(result)
