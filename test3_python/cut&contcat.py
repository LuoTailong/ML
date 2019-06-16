# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

print(pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3,
             retbins=True))

pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3,
       labels=["good", "medium", "bad"])
# [good, good, good, medium, bad, good]
# Categories (3, object): [good < medium < bad]

pd.cut(np.ones(5), 4, labels=False)
# array([1, 1, 1, 1, 1], dtype=int64)

print(pd.qcut(range(5), 3, labels=["good", "medium", "bad"]))

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
print(s1)
print(s2)
print(pd.concat([s1, s2], axis=0))
print(pd.concat([s1, s2], axis=1))

print("="*100)
df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
print(df1)
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
print(df2)
print(pd.concat([df1, df2], ignore_index=True))
print(pd.concat([df1, df2], ignore_index=True, axis=1))
