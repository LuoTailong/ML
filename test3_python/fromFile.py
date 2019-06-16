# -*- coding: utf-8 -*-

import pandas as pd

# file = pd.read_csv("SklearnTest.txt", sep="\t")
file = pd.read_csv("SklearnTest.txt")
print(file)

# 取出height列
print(file.height)
print(file["height"])

# 取出两列
print(file.loc[:, "height": "house"])
print(file.iloc[:, 0: 2])

# 取出0-5行数据
print(file.iloc[0:6, :])
print(file.loc[0:5, :])

# 选择特征列和标签列
x1 = file.loc[:, "height":"job"]
print(x1)
print(type(x1))
y1 = file.loc[:, "is_date"]
print(y1)
print(type(y1))

new_Date = file.query("is_date==-1")
data = file.query("is_date!=-1")
print(new_Date)
print(data)

x = data.iloc[:, 0:5]
y = data.iloc[:, 5]
print(x)
print(type(x))
print(y)
print(type(y))

x = data.drop("is_date", axis=1)
print(x)
print(type(x))

x.to_csv("result.txt", sep=",")
datafile = pd.read_csv("result.txt")
print(datafile)
