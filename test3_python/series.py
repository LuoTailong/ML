# -*- coding: utf-8 -*-
import pandas as pd

# s1 = pd.Series([1, 2, 3, 4, 5])
s1 = pd.Series([1, 2, 3, 4, 5], index=("a", "b", "c", "d", "e"))
print(s1)
print(type(s1))
s2 = pd.Series({1: "apple", 2: "banana", 3: "pear", 4: "orange", 5: "nnn"})
print(s2)
s3 = pd.Series(dict(zip([1, 2, 3, 4, 5], ["apple", "pear", "banana", "orange", "nnn"])))
print(s3)
s4 = pd.Series([1, 2, 3, 4, 5], index=["one", "two", "three", "four", "five"])
print(s4)
print("="*100)
print(s1.shape)
print(s1.ndim)
print(s1.size)
print(s1.dtype)
print(s1.index)
print(s1.values)
print(type(s1.values))
print(s1.head(2))
print(s1.head(3))
print(s1.head(5))

# 取值
print(s1[0])
print(s1["a"])
print(s1[1])
# 更改已有的值
s1["a"] = "abc"
s1[0] = "abc"
print(s1)

# 类别标签列
s5 = pd.Series(["a", "b", "c", "a", "b", "c"])
print(pd.unique(s5))
