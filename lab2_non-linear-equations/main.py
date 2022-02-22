from plt_helper import show_graph
from io_helper import get_table, format_float, output, def_input
from equation_solver import (
    horde_method,
    newton_method,
    simple_iteration_method
)


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
    left, right = map(float, def_input('Границы левого корня через пробел', '-2 0').split())
    r_x0 = float(def_input('Нулевое приближение правого корня', 10))
    eps = float(def_input('Погрешность', 1e-3))
    file_name = def_input('Вывод в файл', None)
    file = open(file_name, 'a') if file_name else None

    lx = horde_method(f, fix=-1, left=left, right=right, eps=eps)
    rx = newton_method(f, df, x0=r_x0, eps=eps)
    cx = simple_iteration_method(f, phi, x0=lx.root, eps=eps)

    roots = (
        ('Левый корень методом хорд', lx),
        ('Центральный корень методом простой итерации', cx),
        ('Правый корень методом Ньютона', rx)
    )

    for title, result in roots:
        output(f'{title}: {format_float(result.root)} (err: {result.error})', file=file)
        output(get_table(result), file=file)

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


if __name__ == '__main__':
    nonlinear_equation_solver()
