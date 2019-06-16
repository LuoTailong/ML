# -*- coding: utf-8 -*-
import numpy as np

randn = np.random.randn(3, 3)
print(randn)
# np.ceil(): 向上最接近的整数，参数是 number 或 array
print(np.ceil(randn))

# np.floor(): 向下最接近的整数，参数是 number 或 array
print(np.floor(randn))

# np.rint(): 四舍五入，参数是 number 或 array
print(np.rint(randn))

# np.isnan(): 判断元素是否为 NaN(Not a Number)，参数是 number 或 array
print(np.isnan(randn))

# np.multiply(): 元素相乘，参数是 number 或 array
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
print(np.multiply(arr1, arr2))

# np.divide(): 元素相除，参数是 number 或 array
print(np.divide(arr1, arr2))

# np.abs()：元素的绝对值，参数是 number 或 array
print(np.abs(randn))

# np.where(condition, x, y): 三元运算符，x if condition else y
print(np.where(arr1 > 0, 1, -1))

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr3)

# 所有元素的和
print(np.sum(arr3))

# 数组的按列统计和
print(np.sum(arr3, axis=0))

# 数组的按行统计和
print(np.sum(arr3, axis=1))

# 列所有元素的平均值 参数是 number 或 array
print(np.mean(arr1))

# 行所有元素的最大值 参数是 number 或 array
print(np.max(arr1, axis=0))
print(np.max(arr1, axis=1))

# 所有元素的标准差 参数是 number 或 array
print(np.std(arr1, axis=0))

# 行所有元素的方差
print(np.var(arr1, axis=0))

# 行最大值的下标索引值 参数是 number 或 array
print(np.argmax(arr1, axis=0))

# 返回一个一维数组，每个元素都是之前所有元素的 累加和 累乘积，参数是 number 或 array
print(np.cumsum(arr3))
print(np.cumprod(arr3))

arr4 = np.array([1, 2, 1, 2, 1, 2, -1, -2, -4])
print(np.unique(arr4, return_inverse=True))

arr5 = np.array([[1, 0, 0], [1, 2, 3], [0, 2, 3]])
print(arr5)
print(np.unique(arr5, axis=0))
print(np.unique(arr5, axis=1))
# np.any(): 至少有一个元素满足指定条件，返回True
# np.all(): 所有的元素满足指定条件，返回True
