# -*- coding: utf-8 -*-

# tuple-->list
t1 = (1, 2, 3, 4)
l1 = list(t1)
print(t1)
print(type(l1))

# set-->list
print(list({1, 3, 4}))

# dict-->list
print(list({"apple": 1, "pear": 2}))
print(list({"apple": 1, "pear": 2}.keys()))
print(list({"apple": 1, "pear": 2}.values()))
print(list({"apple": 1, "pear": 2}.items()))

# list--切片操作
l1 = list(range(10))
print(l1[::])
print(l1[::1])
print(l1[::-1])  # 倒序
print(l1[-2])  # 倒数第二个
print(l1[2:5:])
print(l1[2:5])
print(l1[2:])
print(l1[::2])  # 偶数
print(l1[1::2])  # 奇数

# 补充
print(len(l1))
print([1, 2, 3] + ["one", "A", "B"])
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(list(range(10)))
print(list(range(0, 10, 1)))
print(list(range(0, 10, 2)))

# list--列表--有序--根据下表进行改删查操作
# 创建
l1 = [1, 2, 3, 4, 5, 2]
print(l1)
print(type(l1))
# 查找
print(l1[0])
print(l1[1])
# 修改
l1[0] = "apple"
print(l1)
# 删除
del l1[0]
print(l1)
del l1

# 1、cmp(list1, list2)：比较两个列表的元素 python3中弃用
# 2、len(list)：列表元素个数
# 3、max(list)：返回列表元素最大值
# 4、min(list)：返回列表元素最小值
# 5、list(seq)：将元组转换为列表
# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
l1 = [1, 2, 3, 4, 5, 2]
print(l1.count(2))
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
l1.extend([1, 2, 3, 4, 5])
print(l1)
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
print(l1.index(1))
# 5、list.insert(index, obj)：将对象插入列表
l1.insert(0, "aaa")
print(l1)
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(l1.pop())
print(l1.pop())
print(l1.pop())
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
l1.remove("aaa")
print(l1)
# 8、list.reverse()：反向列表中元素
l1.reverse()
print(l1)
# 9、list.sort([func])：对原列表进行排序
l1.sort()
print(l1)








