# -*- coding: utf-8 -*-
# 猜数字游戏
number = 100
while True:
    guessNumber = int(input("please input your guessNumber:"))
    if guessNumber == number:
        print("you guess right!")
        break
    elif guessNumber > number:
        print("you guess is larger")
        continue
    else:
        print("you guess is smaller")
        continue
