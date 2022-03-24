import numpy as np
import matplotlib.pyplot as plt


def format_float(x):
    return f'{x:.3f}'


def get_table(y, x_from, x_to, num):
    ty = np.vectorize(y)
    xs = np.linspace(start=x_from, stop=x_to, num=num)
    return xs, ty(xs)


def solve(y, x_from, x_to, h):
    num = int((x_to - x_from) / h) + 1
    xs, ys = get_table(y, x_from, x_to, num)

    ############################################

    print('ЛИНЕЙНАЯ АППРОКСИМАЦИЯ')

    print('Таблица')
    print('X', *map(format_float, xs), sep='\t')
    print('Y', *map(format_float, ys), sep='\t')
    SX, SXX, SY, SXY = np.sum(xs), np.sum(xs ** 2), np.sum(ys), np.sum(xs * ys)
    d, d1, d2 = SXX * num - SX * SX, SXY * num - SX * SY, SXX * SY - SX * SXY
    fSX, fSXX, fSY, fSXY = map(format_float, (SX, SXX, SY, SXY))
    print(f'Вычисляем суммы:\nSX = {fSX}, SXX = {fSXX}, SY = {fSY}, SXY = {fSXY}')
    print('Получаем систему линейных уравнений:')
    print(f'{fSXX}a + {fSX}b = {fSXY}')
    print(f'{fSX}a + {num}b = {fSY}')
    print(f'Определители: {d = :.3f}, {d1 = :.3f}, {d2 = :.3f}')
    print('Решая систему, получим значения коэффициентов:')
    a, b = d1 / d, d2 / d
    fa, fb = map(format_float, (a, b))
    print(f'a = {format_float(d1)} / {format_float(d)} = {fa}')
    print(f'b = {format_float(d2)} / {format_float(d)} = {fb}')
    print(f'Проверим правильность линейной модели. '
          f'Вычислим значения функции P(X) = {fa}x + {fb}')
    _, ps = get_table(lambda x: a * x + b, x_from, x_to, num)
    es = ps - ys
    print('X', *map(format_float, xs), sep='\t')
    print('Y', *map(format_float, ys), sep='\t')
    print('P', *map(format_float, ps), sep='\t')
    print('e', *map(format_float, es), sep='\t')

    S = np.sum(es ** 2)
    print(f'Определим меру отклонения: {S = :.3f}')

    ##################################################

    print('=' * 50)
    print('КВАДРАТИЧНАЯ АППРОКСИМАЦИЯ')

    print('Таблица')
    print('X', *map(format_float, xs), sep='\t')
    print('Y', *map(format_float, ys), sep='\t')
    SX, SXX, SXXX, SXXXX, SY, SXY, SXXY = (
        np.sum(xs), np.sum(xs ** 2), np.sum(xs ** 3), np.sum(xs ** 4),
        np.sum(ys), np.sum(xs * ys), np.sum(xs ** 2 * ys)
    )
    fSX, fSXX, fSXXX, fSXXXX, fSY, fSXY, fSXXY = map(format_float,
                                                     (SX, SXX, SXXX, SXXXX, SY, SXY, SXXY))

    print(f'Вычисляем суммы:\n'
          f'SX = {fSX}, SXX = {fSXX}, SXXX = {fSXXX}, SXXXX = {fSXXXX}, '
          f'SY = {fSY}, SXY = {fSXY}, SXXY = {fSXXY}')
    print('Получаем систему линейных уравнений:')
    print(f'{num}a0 + {fSX}a1 + {fSXX}a2 = {fSY}')
    print(f'{fSX}a0 + {fSXX}a1 + {fSXXX}a2 = {fSXY}')
    print(f'{fSXX}a0 + {fSXXX}a1 + {fSXXXX}a2 = {fSXXY}')
    a0, a1, a2 = np.linalg.solve(np.array([[num, SX, SXX], [SX, SXX, SXXX], [SXX, SXXX, SXXXX]]),
                    np.array([SY, SXY, SXXY]))
    print('Решая систему, получим значения коэффициентов:')
    print(f'{a0 = :.3f}, {a1 = :.3f}, {a2 = :.3f}')
    print(f'b = {format_float(d2)} / {format_float(d)} = {fb}')
    print(f'Проверим правильность линейной модели. '
          f'Вычислим значения функции P(X) = {a0:.3f}x^2 + {a1:.3f}x + {a2:.3f}')

    _, ps = get_table(lambda x: a0 * x ** 2 + a1 * x + a2, x_from, x_to, num)
    es = ps - ys
    print('X', *map(format_float, xs), sep='\t')
    print('Y', *map(format_float, ys), sep='\t')
    print('P', *map(format_float, ps), sep='\t')
    print('e', *map(format_float, es), sep='\t')

    S = np.sum(es ** 2)
    print(f'Определим меру отклонения: {S = :.3f}')

    ###########################################################

    bx, by = 3, 3
    x = np.linspace(-bx, bx, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.grid(True)
    plt.xlim((-bx, bx))
    plt.ylim((-by, by))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    p1 = a * x + b
    p2 = a0 * x ** 2 + a1 * x + a2
    ax.plot(x, p1, 'g', label='linear)')
    ax.plot(x, p2, 'r', label='quadratic')

    plt.show()

