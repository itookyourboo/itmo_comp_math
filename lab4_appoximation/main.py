def solve_task1():
    Y = lambda x: 2 * x / (x ** 4 + 7)
    X_FROM, X_TO = 2, 4
    H = 0.2

    import task1
    task1.solve(Y, X_FROM, X_TO, H)


if __name__ == '__main__':
    # solve_task1()
    import approx
    from io_helper import (
        read_data_from_console,
        read_data_from_file,
        output,
        show_graph
    )

    approxes = [
        ('Линейная функция', approx.approx_lin),
        ('Квадратичная функция', approx.approx_quad),
        ('Кубическая функция', approx.approx_cube),
        ('Экспоненциальная функция', approx.approx_exp),
        ('Логарифмическая функция', approx.approx_log),
        ('Степенная функция', approx.approx_pow),
    ]

    read_mode = input('Ввод из файла (_): ').strip()
    read = ((lambda: read_data_from_file(read_mode))
            if read_mode
            else read_data_from_console)
    xs, ys = read()

    results = [a[1](xs, ys) for a in approxes]
    index_min = min(range(len(results)), key=results.__getitem__)

    write_mode = input('Вывод в файл (_): ').strip()
    file = open(write_mode, 'w') if write_mode else None

    out = lambda x: output(x, file)

    for i, result in enumerate(results):
        name = approxes[i][0]
        out(f'--- {name}')
        out(f'φ(x) = {result.function_str}')
        out(f'S = {result.dispersion:.3f}')
        out(f'δ = {result.deviation:.3f}')
        out(f'R^2 = {result.confidence:.3f}')
        if result.pearson:
            out(f'r = {result.pearson:.3f}')

    out(f'Лучше всего аппроксимирует {approxes[index_min][0]}: '
        f'δ = {results[index_min].deviation:.3f}')

    show_graph(xs, ys, results)
