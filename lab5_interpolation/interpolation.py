from math import factorial


def lagrange_polynomial(dots, x):
    result = 0

    n = len(dots)
    for i in range(n):
        nom, denom = 1, 1
        for j in range(n):
            if i == j:
                continue
            nom *= x - dots[j][0]
            denom *= dots[i][0] - dots[j][0]
        result += dots[i][1] * nom / denom

    return result


def gauss_t(t, n):
    tmp = t
    for i in range(1, n):
        tmp *= t + ((-1) ** i) * ((i + 1) // 2)
    return tmp


def gauss_polynomial(dots, x):
    n = len(dots)
    y = [[0 for _ in range(n)] for __ in range(n)]
    for k in range(n):
        y[k][0] = dots[k][1]

    for i in range(1, n):
        for j in range(n - 1):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    result = y[n // 2][0]
    t = (x - dots[n // 2][0]) / (dots[1][0] - dots[0][0])
    for i in range(1, n):
        result += gauss_t(t, i) * y[(n - i) // 2][i] / factorial(i)

    return result


def stirling_polynomial(dots, x):
    n = len(dots)
    y = [[0 for _ in range(n)] for __ in range(n)]
    for k in range(n - 1):
        y[k][0] = dots[k + 1][1] - dots[k][1]

    for i in range(1, n - 1):
        for j in range(n - i - 1):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    result = y[n // 2][0]
    s = n // 2
    t = (x - dots[s][0]) / (dots[1][0] - dots[0][0])

    k, d, l = 1, 1, 1
    tmp1, tmp2 = 1, 1

    for i in range(1, n):
        d *= i
        s = (n - i) // 2
        if i % 2:
            if k != 2:
                tmp1 *= t ** k - (k - 1) ** 2
            else:
                tmp1 *= t ** 2 - (k - 1) ** 2
            k += 1
            result += (tmp1 / (2 * d)) * (y[s][i - 1] + y[s - 1][i - 1])
        else:
            tmp2 *= t ** 2 - (l - 1) ** 2
            l += 1
            result += tmp2 / d * y[s][i - 1]

    return result
