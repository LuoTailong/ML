# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

s1 = pd.Series(range(12), index=[
    ["a", "a", "a", "b", "b", "b", "c", "c", "c", "d", "d", "d"],
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
])
print(s1)
print(s1["a"][1])
s1["a"][1] = 100
print(s1)
print(s1.swaplevel())
print(s1.swaplevel().sortlevel())

print(s1["a"])
print(s1[0])
print(s1[1])
print(s1["a"][1])
