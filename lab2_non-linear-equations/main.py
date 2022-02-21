# #### Решение нелинейных уравнений
# - Метод Ньютона
# - Метод простой итерации
#
# #### Решение систем нелинейных уравнений
# - Метод простой итерации


def print_values(iteration, values, sep='\t\t', digits=3):
    print(iteration, *map(lambda x: f'{x:.{digits}f}', values), sep=sep)


EPS = 1e-2


def horde_method(func, fix=-1, left=7, right=10):
    print('№', 'a', '\tb', '\tx', '\tf(a)', 'f(b)', 'f(x)', '|a-b|', sep='\t\t')
    x0 = left if fix == -1 else right
    iteration = 1
    while True:
        x1 = (left * func(right) - right * func(left)) / (func(right) - func(left))

        print_values(iteration, values=[
            left, right, x1, func(left), func(right), func(x1), abs(left - right)
        ])

        if (
                abs(x1 - x0) <= EPS / 10 or
                abs(func(x1)) <= EPS
        ):
            return x1

        if func(x1) * func(left) < 0:
            right = x1
        else:
            left = x1

        x0 = x1
        iteration += 1


def newton_method(func, dfunc, x0=10):
    print('№', 'x_k', '\tf(x_k)', 'f\'(x_k)', 'x_{k+1}', '|x_k-x_{k+1}|', sep='\t\t')
    iteration = 1
    while True:
        x1 = x0 - func(x0) / dfunc(x0)

        print_values(iteration, [
            x0, func(x0), dfunc(x0), x1, abs(x1 - x0)
        ])

        if (
                abs(x1 - x0) <= EPS or
                abs(func(x1) / dfunc(x1)) <= EPS or
                abs(func(x1)) <= EPS
        ):
            return x1

        x0 = x1
        iteration += 1


def simple_iteration_method(func, pfunc, x0=1):
    print('№', '\tx_k', '\t\tf(x_k)', '\tx_{k+1}', '\tphi(x_k)', '|x_k-x_{k+1}|', sep='\t')
    iteration = 1
    while True:
        x1 = pfunc(x0)

        print_values(iteration, [
            x0, func(x0), x1, pfunc(x0), abs(x1 - x0)
        ])

        if (
                abs(x1 - x0) <= EPS
        ):
            return x1

        x0 = x1
        iteration += 1


A, B, C, D = 1, -3.78, 1.25, 3.49


def f(x):
    return A * x ** 3 + B * x ** 2 + C * x + D


def phi(x):
    base = -(B * x ** 2 + C * x + D) / A
    if base < 0:
        return -(-base) ** (1 / 3)
    return base ** (1 / 3)


def df(x):
    return 3 * A * x ** 2 + 2 * B * x + C


if __name__ == '__main__':
    r_x = horde_method(f, fix=-1, left=-2, right=0)
    print('Краний правый корень методом хорд:', r_x)
    l_x = newton_method(f, df)
    print('Краний левый корень методом Ньютона:', l_x)
    c_x = simple_iteration_method(f, phi, x0=1)
    print('Центральный корень методом простой итерации:', c_x)

    print('Корни: ', *map(lambda x: f'{x:.3f}', [
        l_x, c_x, r_x
    ]))
