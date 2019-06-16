# -*- coding: utf-8 -*-
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

mb.showinfo("welcome", "guessGame")
number = 100
while True:
    guessNumber = dl.askinteger("Ask Integer:", "please input yout guessNumber:")
    if guessNumber == number:
        mb.showinfo("", "you guess right!")
        break
    elif guessNumber > number:
        mb.showinfo("", "you guess is larger")
        continue
    else:
        mb.showinfo("", "you guess is smaller")
        continue
