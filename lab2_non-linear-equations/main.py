from math import sin, exp

from plt_helper import show_graph
from io_helper import (
    get_result_table,
    format_float,
    output,
    def_input,
    get_intervals_table,
    get_root_table
)
from equation_solver import (
    horde_method,
    newton_method,
    simple_iteration_method,
    get_interval_values,
    get_interval_roots
)
from system_solver import system_simple_iteration_method


A, B, C, D = 1, -3.78, 1.25, 3.49
f = lambda x: A * x ** 3 + B * x ** 2 + C * x + D
df = lambda x: 3 * A * x ** 2 + 2 * B * x + C


def phi(x):
    base = -(B * x ** 2 + C * x + D) / A
    if base < 0:
        return -(-base) ** (1 / 3)
    return base ** (1 / 3)


def nonlinear_equation_solver():
    output('Функция: x^3 - 3.78x^2 + 1.25x + 3.49')
    file_name = def_input('Вывод в файл', None)
    file = open(file_name, 'a') if file_name else None

    interval = get_interval_values(-2, 3, 0.5, f, df)
    output('Интервалы', file)
    output(get_intervals_table(interval), file)
    roots = get_interval_roots(interval)
    output('Корни', file)
    output(get_root_table(roots), file)

    left, right = map(float, def_input('Границы левого корня через пробел', '-2 0').split())
    r_x0 = float(def_input('Нулевое приближение правого корня', 10))
    c_x0 = float(def_input('Нулевое приближение центрального корня', -0.5))
    eps = float(def_input('Погрешность', 1e-2))

    lx = horde_method(f, fix=-1, left=left, right=right, eps=eps)
    rx = newton_method(f, df, x0=r_x0, eps=eps)
    cx = simple_iteration_method(f, phi, x0=c_x0, eps=eps)

    roots = (
        ('Левый корень методом хорд', lx),
        ('Центральный корень методом простой итерации', cx),
        ('Правый корень методом Ньютона', rx)
    )

    for title, result in roots:
        output(f'{title}: {format_float(result.root)} (err: {result.error})', file=file)
        output(get_result_table(result), file=file)

    output('Корни: ' + ' '.join(map(format_float, [
        lx.root, cx.root, rx.root
    ])), file=file)

    bx = max(abs(lx.root), abs(rx.root)) + 1
    by = abs(f(bx))

    show_graph(bx, by, f, points=[
        (lx.root, 0), (cx.root, 0), (rx.root, 0)
    ])

    if file:
        file.close()


FUNCTIONS = [
    (
        (
            'f1(x1, x2) = 0.1 * x1^2 + x1 + 0.2 * x2^2 - 0.3',
            lambda x1, x2: 0.3 - 0.1 * x1 ** 2 - 0.2 * x2**2,
            lambda x1, x2: 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3
        ),
        (
            'f1(x1, x2) = x1 - sin(2 * x2^2 + 3)',
            lambda x1, x2: sin(2 * x2 ** 2 + 3),
            lambda x1, x2: x1 - sin(2 * x2 ** 2 + 3)
        )
    ),
    (
        (
            'f2(x1, x2) = 0.2 * x1^2 + x2 + 0.1 * x1 * x2 - 0.7',
            lambda x1, x2: 0.7 - 0.2 * x1 ** 2 - 0.1 * x1 * x2,
            lambda x1, x2: 0.2 * x1 ** 2 + x2 + 0.1 * x1 * x2 - 0.7
        ),
        (
            'f2(x1, x2) = exp(x1^3 - 8 * x1^2) + 4 * x2',
            lambda x1, x2: -exp(x1 ** 3 - 8 * x1 ** 2) / 4,
            lambda x1, x2: exp(x1 ** 3 - 8 * x1 ** 2) + 4 * x2
        )
    )
]


def system_solver():
    x = []
    y = []
    for i, group in enumerate(FUNCTIONS, 1):
        print(f'Выберите функцию №{i}')
        print(*(f'{j}. {fun[0]}' for j, fun in enumerate(group, 1)), sep='\n')
        n = int(input())
        x.append(group[n - 1][1])
        y.append(group[n - 1][2])

    x0 = list(map(float, def_input('Начальные приближения', ' '.join(['1' for _ in x])).split()))
    eps = float(def_input('Погрешность', 1e-3))
    file_name = def_input('Вывод в файл', None)
    file = open(file_name, 'a') if file_name else None

    res = system_simple_iteration_method(x, x0, eps)

    if res.solved:
        output('Решение: ' + ' '.join(format_float(x) for x in res.roots), file=file)
        output('Погрешности: ' + ' '.join(str(x) for x in res.errors), file=file)
        output(f'Количество итераций {res.iteration}', file=file)
    else:
        output('Решений не найдено', file=file)

    if file:
        file.close()

    bx = abs(min(res.roots)) + 1
    show_graph(bx, 0, y, [])


if __name__ == '__main__':
    nonlinear_equation_solver()
    system_solver()
