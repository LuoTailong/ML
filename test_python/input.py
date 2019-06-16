# -*- coding: utf-8 -*-

# 科学计数法
print(3.14e2)
print(3.14e-2)

# 字符串引用
str4 = '哈哈'
str5 = "哈哈"
str6 = '''\
哈哈1
哈哈2
哈哈3\
'''
print(str4)
print(str5)
print(str6)

age = int(input("Please input your age:"))
print(age)
print(type(age))
name = "张三"
age = 100
print("name is:", name, "age is:", age)
print("name is:" + name, "age is:" + str(age))
print("name is:{},age is:{}".format(name, age))
print("name is:{0},age is {1}".format(name, age))
print("name is:%s,age is:%d" % (name, age))
