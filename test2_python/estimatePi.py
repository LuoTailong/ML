# -*- coding: utf-8 -*-
import random


# times是落入正方形内的次数
# hits是落入圆形内的次数
def estimatePi(times):
    hits = 0
    for i in range(times):
        x = random.random() * 2 - 1  # x = random.random()也行
        y = random.random() * 2 - 1  # y = random.random()也行
        if x ** 2 + y ** 2 < 1:
            hits += 1
    return 4.0 * hits / times


if __name__ == '__main__':
    PI = estimatePi(10000)
    print(PI)
