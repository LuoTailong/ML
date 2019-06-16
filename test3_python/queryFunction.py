# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
print(df1)
print(df1.query("b>c"))
print(df1.query("c>b"))
