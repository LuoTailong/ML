# -*- coding: utf-8 -*-
from OrentArithmath import Arithmatic

x = int(input("please input a number:"))
y = int(input("please input another number:"))
arith = Arithmatic(x, y)
print(arith.add())
print(arith.sub())
print(arith.mul())
print(arith.div())
