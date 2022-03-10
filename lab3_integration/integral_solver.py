import numpy as np


class RectAlign:
    LEFT = -1
    MID = 0
    RIGHT = 1


def rect_method(f, a, b, align=0, num=100):
    h = (b - a) / num
    arr = np.linspace(a, b, num, endpoint=False)
    match align:
        case -1:
            res = h * sum(f(x) for x in arr)
        case 0:
            res = sum(h * f(x + h / 2) for x in arr)
        case 1:
            res = sum(h * f(x + h) for x in arr)
        case _:
            raise ValueError('incorrect align')

    return res


def trapeze_method(f, a, b, num=100):
    h = (a + b) / num
    arr = np.linspace(a, b, num, endpoint=False)
    return h * ((f(a) + f(b)) / 2 + sum(f(x) for x in arr))


def runge_err(res, res2, k):
    return abs(res2 - res) / (2 ** k - 1)
