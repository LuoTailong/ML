def fileWriter():
    sentence = '''
this is my coumputer
this is my thinkpad
this is my ct 
'''
    # f = open("sen.txt", mode="w")
    # f.writelines(sentence)
    # f.close()
    # 等价于
    with open("sen.txt", mode="w") as f:
        f.writelines(sentence)


def fileReader():
    f = open("sen.txt", mode="r")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")


# -*- coding: utf-8 -*-
if __name__ == '__main__':
    fileWriter()
    fileReader()
    # pass
