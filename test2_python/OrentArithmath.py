# -*- coding: utf-8 -*-
class Arithmatic():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def add(self):
        return self.X + self.Y

    def sub(self):
        return self.X - self.Y

    def mul(self):
        return self.X * self.Y

    def div(self):
        return self.X / self.Y


if __name__ == '__main__':
    X = int(input("please input a number:"))
    Y = int(input("please input another number:"))
    arith = Arithmatic(X, Y)
    print(arith.add())
    print(arith.sub())
    print(arith.mul())
    print(arith.div())
