# -*- coding: utf-8 -*-
import pandas as pd
# one-hot编码形式
s = pd.Series(list('abca'))
print(s)
print(pd.get_dummies(s))
#    a  b  c
# 0  1  0  0
# 1  0  1  0
# 2  0  0  1
# 3  1  0  0
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print(df)
print(pd.get_dummies(df, prefix=['col1', 'col2']))
