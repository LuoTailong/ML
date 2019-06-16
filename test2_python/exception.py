# -*- coding: utf-8 -*-

try:
    print(2 / 0)
except ZeroDivisionError:
    print("division can not be 0")
finally:
    print("Finish")

try:
    age = int(input("please input your age:"))
except ValueError:
    print("input again")
finally:
    print("Finish")

number = 100
while True:
    try:
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
    except:
        print("input again")
    finally:
        print("Done")
