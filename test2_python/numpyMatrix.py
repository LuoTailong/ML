# -*- coding: utf-8 -*-
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 矩阵乘法
print(np.dot(arr1, arr1))
print(arr1.dot(arr1))
# 矩阵转置
print(arr1.T)
print(arr1.T.dot(arr1))

# 矩阵行列式
from numpy.linalg import det

print("行列式", det(arr1))
arr2 = np.array([[1, 2], [2, 4]])
print(det(arr2))

# 矩阵求逆--伴随矩阵求行列式--行列式为0的话 整个求逆的结果不存在
from numpy.linalg import inv

print(inv(arr1))

# 矩阵分解--QR分解
from numpy.linalg import qr

Q, R = qr(arr1)
print(Q)
print(R)
print(Q.dot(R))
# 矩阵分解--特征值分解
from numpy.linalg import eig

value, vector = eig(arr1)
print(value)
print(vector)

# 如何将特征值转换为特征向量
# A=Vector*Value*inv(Vector)
# np.diag(value)可以把value转换成3行3列
print(vector.dot(np.dot(np.diag(value), inv(vector))))

# 矩阵分解--奇异值分解
print("-----------------------")
from numpy.linalg import svd

U, Sigma, VT = svd(arr1)
print(U)
print(Sigma)
print(VT)

# 是否正交
print(U.dot(inv(U)))
print(VT.dot(inv(VT)))

# 转换回去
print(np.dot(U, np.dot(np.diag(Sigma), VT)))
print(np.allclose(np.dot(U, np.dot(np.diag(Sigma), VT)), arr1))
