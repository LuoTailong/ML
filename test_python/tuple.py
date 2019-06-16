# -*- coding: utf-8 -*-
# tuple--元组--有序--根据下表进行查，不能修改和删除
# 定义只有一个元素的tuple

# 创建
t0 = (1,)
print(type(t0))
t1 = (1, 2, 3, 4, 5)
t2 = tuple(range(10))
t3 = tuple([1, 2, 3, 4])
t4 = tuple({1, 2, 3, 4})
t5 = tuple({1: "apple", 2: "banana", 3: "orange"})
print(t1)
print(type(t1))
print(t2)
print(t3)
print(t4)
print(t5)

# 如果在tuple中定义一个list 那么list是否可以改变呢
t6 = (1,2,3,["apple","pear"])
print(t6)
print(t6[0])
print(t6[1])
print(t6[2])
print(t6[3][0])
print(t6[3][1])
t6[3][0] = "banana"
print(t6)

# 查找
print(t1[0])
print(t1[1])
# 修改
# t1[0]="apple"
# print("修改后的值：{}".format(t1))
# 删除
# del t1[0]

# 查找--切片操作
print(t1[::-1])
print(t1)
print(t1[0:len(t1):1])
print(t1[0:len(t1)])
print(t1[0:])
print(t1[::])
print(t1[0:4])
print(t1[0:4:1])

