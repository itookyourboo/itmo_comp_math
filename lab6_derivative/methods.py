def improved_euler_method(eq, h):
    n = int((eq.b - eq.a) / h)
    x, y = [eq.a], [eq.y0]
    for i in range(n):
        y0 = y[i] + h / 2 * eq.dif(x[i], y[i])
        y.append(y[i] + h * eq.dif(x[i] + h / 2, y0))
        x.append(x[i] + h)

    return x, y


def adams_method(eq, h):
    n = int((eq.b - eq.a) / h)
    x, y = improved_euler_method(eq, h)
    # x, y = [eq.a], [eq.y0]
    # for i in range(n):
    #     x.append(x[i] + h)
    #     y.append(y[i] + h * eq.dif(x[i], y[i]))

    f = eq.dif
    for i in range(3, len(x)):
        k = [f(x[i - q], y[i - q]) for q in range(4)]
        df = k[0] - k[1]
        d2f = k[0] - 2 * k[1] + k[2]
        d3f = k[0] - 3 * k[1] + 3 * k[2] - k[3]
        y[i] = (
            y[i - 1] +
            1 * h ** 1 * k[1] +
            1 * h ** 2 * df / 2 +
            5 * h ** 3 * d2f / 12 +
            3 * h ** 4 * d3f / 8
        )

    return x, y


def runge_rule(yh, y2h, p):
    return abs((yh - y2h) / (2 ** p - 1))
