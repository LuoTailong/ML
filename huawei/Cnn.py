import time

A_LEVEL = 4
B_LEVEL = 4


def cnn():
    global A_LEVEL
    global B_LEVEL

    a_xishu = list()
    b_xishu = list()

    for i in range(A_LEVEL + 1):
        one = list()
        one.append(int(input()))
        one.append(int(input()))
        a_xishu.append(one)

    for i in range(B_LEVEL + 1):
        two = list()
        two.append(int(input()))
        two.append(int(input()))
        b_xishu.append(two)

    a_xishu = a_xishu[::-1]
    b_xishu = b_xishu[::-1]

    star_t = time.time()
    a_len = len(a_xishu)
    b_len = len(b_xishu)
    top_level = A_LEVEL + B_LEVEL
    for i in range(top_level + 1)[::-1]:
        ci_s = 0
        ci_x = 0
        for index in range(i + 1)[::-1]:
            if i - index < a_len and index < b_len:
                temp = fsm(a_xishu[i - index], b_xishu[index])
                ci_s += temp[0]
                ci_x += temp[1]
        print(ci_s)
        print(ci_x)
    print("耗时: {}".format(time.time() - star_t))


def fsm(x, y):
    s = x[0] * y[0] - x[1] * y[1]
    x = x[0] * y[1] + x[1] * y[0]
    return s, x


cnn()
