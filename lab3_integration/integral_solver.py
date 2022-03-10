import numpy as np


class RectAlign:
    LEFT = -1
    MID = 0
    RIGHT = 1


def rect_method(f, a, b, align=0, num=100):
    h = (b - a) / num
    arr = np.linspace(a, b, num, endpoint=False)
    match align:
        case RectAlign.LEFT:
            res = h * sum(f(x) for x in arr)
        case RectAlign.MID:
            res = sum(h * f(x + h / 2) for x in arr)
        case RectAlign.RIGHT:
            res = sum(h * f(x + h) for x in arr)
        case _:
            raise ValueError('incorrect align')

    return res


def trapeze_method(f, a, b, num=100):
    h = (b - a) / num
    arr = np.linspace(a, b, num, endpoint=False)[1:]
    return h * ((f(a) + f(b)) / 2 + sum(f(x) for x in arr))


def runge_err(res, res2, k):
    return abs(res2 - res) / (2 ** k - 1)


def inf_or_err(f, num):
    try:
        res = f(num)
        return np.isinf(res)
    except Exception:
        return True


def diverges(f, a, b):
    return inf_or_err(f, a) or inf_or_err(f, b)


def normalized_rect_method(f, F, a, b, align=0, num=100):
    if diverges(F, a, b):
        return None

    try:
        res = rect_method(f, a, b, align, num)
        if np.isinf(res):
            return None
    except:
        return None

    return res


def normalized_trapeze_method(f, F, a, b, num=100):
    if diverges(F, a, b):
        return None

    try:
        res = trapeze_method(f, a, b, num)
        if np.isinf(res):
            return None
    except:
        return None

    return res
