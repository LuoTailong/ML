# -*- coding: utf-8 -*-
# dict--字典--无序--根据下标进行查删改的操作 键必须唯一有相同键后面覆盖前面
# 创建
d1 = {"apple": 1, "pear": 1, "orange": 2}
print(d1)
print(type(d1))

d2 = dict(name="zhangsan", age=13)
print(d2)
print(type(d2))

d3 = dict(zip(["apple", 'pear'], [10, 20]))
print(d3)

# 查找
print(d1["apple"])
# 修改
d1["apple"] = 100
print("修改后的值：{}".format(d1))
# 删除
del d1["apple"]
print(d1)

# 没有hash值或可改变类型都不能作为键 如list不可以tuple可以
# print(hash(["zhangsan"]))  # TypeError: unhashable type: 'list'
print(hash(("zhangsan")))
d4 = {("zhangsan"): 100, "lisi": 200, "wnagwu": 300}
print(d4)

# 1、cmp(dict1, dict2)：比较两个字典元素。python3弃用
# 2、len(dict)：计算字典元素个数，即键的总数。
# 3、str(dict)：输出字典可打印的字符串表示。
# 4、type(variable)：返回输入的变量类型，如果变量是字典就返回字典类型。
# Python字典包含了以下内置方法：
# 1、radiansdict.clear()：删除字典内所有元素
# 2、radiansdict.copy()：返回一个字典的浅复制
# 3、radiansdict.fromkeys()：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
#  如：print "fromkeys",dict_2.fromkeys(dict_2,irisPro)
# 4、radiansdict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
# 5、radiansdict.has_key(key)：如果键在字典dict里返回true，否则返回false
# 6、radiansdict.items()：以列表返回可遍历的(键, 值) 元组数组
# 7、radiansdict.keys()：以列表返回一个字典所有的键
# 8、radiansdict.setdefault(key, default=None)：和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
# 9、radiansdict.update(dict2)：把字典dict2的键/值对更新到dict里
# irisPro、radiansdict.values()：以列表返回字典中的所有值
