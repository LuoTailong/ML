# -*- coding: utf-8 -*-

import random
import numpy as np

print(random.random)
print(random.randint(1, 10))
print(random.randrange(1, 10, 1))

print(np.random.rand(100, 100))
print(np.random.chisquare(10, size=(5, 5)))

print(range(10))
print(type(range(10)))
