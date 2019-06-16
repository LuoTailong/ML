# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(3, 3))
print(df1)

df1.columns = ["one", "two", "three"]
print(df1)
df2 = pd.DataFrame(np.random.randn(3, 3), columns=["one", "two", "three"])
print(df2)
df3 = pd.DataFrame(np.random.randn(3, 3), columns=["one", "two", "three"], index=["a", "b", "c"])
print(df3)

print(df1.shape)
print(df1.ndim)
print(df1.size)
print(df1.dtypes)
print(df1.index)
print(df1.columns)
print(type(df1.values))
print(df1.head())
print(df1.tail())
print(df1.info())

# iloc必须用数字索引 loc必须用自己设定的索引
print("=" * 100)
print(df1.iloc[0, :])

print("=" * 100)
print(df1.iloc[0:2, 0:2])
print(df3.loc["a":"c", "one":"three"])
print(df1.loc[0:2, "one":"two"])
print(df1.loc[:, lambda df: ["one", "two"]])

# 查找df1的所有行所有列
print("=" * 100)
print(df1.loc[:, :])

# 查找数据集df1中为"one"的这一列
print("=" * 100)
print(df1["one"])
print("=" * 100)
print(df1.one)

# 查找数据集df1中的第1行1列的元素
print("=" * 100)
print(df1.loc[0, "one"])

# 查找第一行元素
print("=" * 100)
print(df1.loc[0, :])

# 更改
df1.iloc[0, 0] = 100
print(df1)
df1.loc[0, "one"] = 1000
print(df1)

# 删除操作
del df1["one"]
print(df1)

# 增加一列
df1["D"] = [1, 2, 3]
print(df1)
