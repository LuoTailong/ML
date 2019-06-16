# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# 对齐运算
s1 = pd.Series(range(5), index=range(5))
s2 = pd.Series(range(10), index=range(10))

print(s1 + s2)
print("="*100)
print(s1.add(s2, fill_value=100))

df1 = pd.DataFrame(np.ones(shape=(2, 2)), columns=["one", "two"])
df2 = pd.DataFrame(np.ones(shape=(3, 3)), columns=["one", "two", "three"])
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2, fill_value=100))
