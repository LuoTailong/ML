# -*- coding: utf-8 -*-
import numpy as np

r1 = np.matrix([1, 2, 3, 4])
print(r1)
print(r1.ndim)
print(r1.shape)
print(r1.size)
r2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(r2)
print(r2.ndim)
print(r2.shape)
print(r2.size)
r3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(r3)
print(r3.ndim)
print(r3.shape)
print(r3.size)

# mat是matrix的别名
r3 = np.mat([1, 2, 3, 4])
print(r3)
r4 = np.mat("1,2;3,4")
print(r4)
