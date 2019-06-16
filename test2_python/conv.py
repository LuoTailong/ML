# -*- coding: utf-8 -*-
import scipy as sp

result = sp.convolve([1, 2, 3, 4], [4, 5, 6])
print(result)


def conv(lst1, lst2):
    length1 = len(lst1)
    length2 = len(lst2)

    lst1.reverse()
    result = []
    for i in range(1, length1 + 1):
        t = lst1[length1 - i:]
        r1 = sum([t1 * t2 for t1, t2 in zip(t, lst2)])
        result.append(r1)

    for i in range(1, length2):
        t = lst2[i:]
        r2 = sum([t1 * t2 for t1, t2 in zip(lst1, t)])
        result.append(r2)
    return result


if __name__ == '__main__':
    result = conv([1, 2, 3, 4], [4, 5, 6])
    print(result)
