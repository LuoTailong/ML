# -*- coding: utf-8 -*-
import numpy as np

r1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(r1))
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(arr1))
print(arr1)

print("shape", arr1.shape)
print("shape", arr1.ndim)  # 向量--维度1 矩阵--维度2 数组--维度3
print("dtype", arr1.dtype)
print("dtype", arr1.size)

# 其他数据类型的转换
print(np.array((1, 2, 3, 4)))
print(np.array({1, 2, 3, 4}))
print(np.array({1: "apple", 2: "banana"}))

r1 = np.zeros(shape=(3, 3))
print(r1)
r2 = np.ones(shape=(3, 3))
print(r2)
A = np.diag([1, 2, 3, 4])
print(A)

print(np.fliplr(A))
print(np.eye(2, dtype=int))
print(np.diagflat([[1, 2], [3, 4]]))
print(np.tri(3, 5, 2, dtype=int))
print(np.tril([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], -1))
