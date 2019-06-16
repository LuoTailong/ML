# -*- coding: utf-8 -*-
import numpy as np

# 等差数列
r1 = np.linspace(1, 10, num=10)
print(r1)
r2 = np.linspace(1, 10, num=50)
print(r2)
# 等比数列
r3 = np.logspace(1, 10, 10)
print(r3)
r4 = np.logspace(1, 10, 11)  # 从1到10 共11个数的等比数列
print(r4)
