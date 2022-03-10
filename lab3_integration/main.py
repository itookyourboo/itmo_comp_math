from integral_solver import rect_method, trapeze_method, runge_err

f = lambda x: -x ** 3 - x ** 2 - 2 * x + 1
k = 2
f_str = "-x^3 - x^2 - 2x + 1"
I_EXACT = -26 / 3


def main():
    print(f'''Выберите метод для вычисления интеграла функции: {f_str}
    1. Метод левых прямоугольников
    2. Метод средних прямоугольников
    3. Метод правых прямоугольников
    4. Метод трапеций'''
          )
    method = int(input())
    if not 1 <= method <= 4:
        print('Неверное значение')
        main()

    a, b = map(float, input('Введите границы интегрирования через пробел: ').split())
    n = int(input('Введите число разбиений: '))
    fun = None
    err_f = 0

    match method:
        case 1 | 2 | 3:
            fun = lambda: rect_method(f, a, b, method - 2, n)
            err_f = lambda: rect_method(f, a, b, method - 2, n // 2)
        case 4:
            fun = lambda: trapeze_method(f, a, b, n)
            err_f = lambda: trapeze_method(f, a, b, n // 2)

    res = fun()
    print('Результат вычисления:', res)
    print('Число разбиений:', n)

    if (a, b) == (0, 2):
        err_abs = abs(I_EXACT - res)
        print(f'Погрешность: {err_abs:.4f} ({abs(err_abs / I_EXACT):.2f}%)')

    res2 = err_f()
    err = runge_err(res, res2, k)
    print(f'Погрешность по правилу Рунге: {err:.4f}')


if __name__ == '__main__':
    main()
