import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from lab6_derivative.methods import improved_euler_method, adams_method, runge_rule
from lab6_derivative.util import Equation, Fun, format_float as ff

EQUATIONS = [
    Equation(
        dif=Fun('y + (1 + x) * y ** 2'),
        ex=Fun('-1 / x'),
        a=1,
        b=1.5,
        y0=-1
    ),
    Equation(
        dif=Fun('3 * x ** 2 * y + x ** 2 * exp(x ** 3)'),
        ex=Fun('x ** 3 * exp(x ** 3) / 3'),
        a=0,
        b=1,
        y0=0
    ),
    Equation(
        dif=Fun('cos(x) - y'),
        ex=Fun('(cos(x) + sin(x)) / 2'),
        a=0,
        b=0.1,
        y0=0.5
    )
]

METHODS = [
    ('Усовершенствованный метод Эйлера', improved_euler_method, 2),
    ('Метод Адамса', adams_method, 4)
]


def main():
    for i, eq in enumerate(EQUATIONS, 1):
        print(f"{i}.\ty' = {eq.dif!s}\n"
              f"\tx[{eq.a}; {eq.b}], y({eq.a}) = {eq.y0}")
    eq = EQUATIONS[int(input('Выберите дифференциальное уравнение: ')) - 1]

    for i, (name, *_) in enumerate(METHODS, 1):
        print(f"{i}. {name}")
    method = METHODS[int(input('Выберите метод решения: ')) - 1]
    fun, p = method[1], method[2]

    h = float(input('Выберите шаг: '))

    x, y = fun(eq, h)
    f_dif = [eq.dif(xi, yi) for xi, yi in zip(x, y)]
    f_ex = [eq.ex(xi) for xi in x]
    eps = [abs(yi - ex) for yi, ex in zip(y, f_ex)]

    table = PrettyTable(['i', 'x', 'y', 'f(x, y)', 'Точное решение', 'eps'])
    table.add_rows([
        (i, ff(x[i]), ff(y[i]), ff(f_dif[i]), ff(f_ex[i]), ff(eps[i]))
        for i in range(len(x))
    ])
    print(table)

    runge = runge_rule(y[-1], fun(eq, 2 * h)[1][-1], p)

    print('Погрешность:', max(eps))
    print('По Рунге:', runge)

    x_ex = np.linspace(eq.a, eq.b)
    y_ex = np.vectorize(eq.ex)(x_ex)

    plt.title(f"y' = {eq.dif}")
    plt.plot(x_ex, y_ex, 'blue', label=f"y = {eq.ex}")
    plt.plot(x, y, 'go--', label="Численное решение")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
