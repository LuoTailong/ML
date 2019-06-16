# -*- coding: utf-8 -*-
# zip函数作用就是将不同组的各个对应元素进行组合
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4, 5, 6]
print(list(zip(l1, l2)))
print(list(zip([9, 10, 11], [1, 2, 3])))
# enumerate函数--枚举
print(list(enumerate(range(10), start=10)))
