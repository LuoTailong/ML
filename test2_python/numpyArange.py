# -*- coding: utf-8 -*-
import numpy as np

print(list(range(1, 10, 3)))
r1 = np.arange(10)
print(r1)
print(type(r1))
print(np.array(np.random.randn(3, 3)))
# shape
r1.shape = 2, 5
print(r1)

print(np.arange(10).reshape(2, 5))

r2 = r1.astype(np.float)
print(r1.dtype)
print(r2.dtype)
