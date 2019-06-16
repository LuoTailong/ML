# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(5, 4), index=("a", "b", "c", "d", "e"), columns=("A", "B", "C", "D"))
print(df1)

# skipna 排除缺失值 默认为True
print(df1.sum(axis=1))
print(df1.sum(axis=0))
print(df1.mean(axis=1))
print(df1.mean(axis=0))
print(df1.max(axis=1))
print(df1.describe())
print(df1)
print(df1.query("A>B"))
print(df1.count())
print(df1.quantile())  # 计算样本的分位数
print(df1.mean(axis=0))  # 均值
print(df1.median())  # 中位数
# mad 平均绝对离差
# var 样本方差
# std 样本的标准差
# skew 样本值的偏度----正态分布的偏度为0
# kurt 样本值的峰度------正态分布的峰度为3
# cumsum样本值的累计和
print(df1)
print(df1.cumsum())
