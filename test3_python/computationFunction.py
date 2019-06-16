# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df1 = pd.DataFrame([[np.nan, 2, 3], [2, np.nan, 3], [3, 4, 5]])
print(df1)

# isnull
print(df1.isnull())
print(df1.fillna(100))

print(df1.drop([0], axis=0))
print(df1.drop([0], axis=1))
print(df1.dropna(axis=0))
print(df1.dropna(axis=1))

print(df1.apply(lambda x: x.max(axis=0)))
# print(df1.apply(lambda x: x.max(axis=1)))
print(df1.apply(lambda x: (x - x.mean() / x.std()), axis=1))

df1.columns = ["one", "two", "three"]
print(df1.sort_values(by="three", axis=0, ascending=False))

print(df1.sort_index(axis=0))
