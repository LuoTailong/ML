# -*- coding: utf-8 -*-
X = 60


def printLg(X):
    print("Current x value is:{}".format(X))
    X = 100
    print("Change X value is:%d" % (X))

    printLg(X)
    print("Final X result is:", X)

    X = 100

    def printLg1():
        global X
        print("Current X value is:{}".format(X))
        X = 200
        print("Change X value is:" + str(X))

printLg1()
print("Final X value is:"+X)