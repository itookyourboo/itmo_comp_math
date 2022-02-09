import io_helper
import sys

from kuhn import make_matrix_diagonal_dominance


LIMIT = 5000
EPSILON = 1e-6
PRECISION = 6


def converges(vars_old, vars_new, eps):
    n = len(vars_old)
    return sum((vars_new[i] - vars_old[i]) ** 2 for i in range(n)) ** 0.5 < eps


def seidel_iteration(coefficients, vars, values):
    n = len(coefficients)
    vars = vars[:]

    for i in range(n):
        s = sum(coefficients[i][j] * vars[j] for j in range(n) if i != j)
        vars[i] = (values[i] - s) / coefficients[i][i]

    return vars


def solve(coefficients, values, epsilon, precision=PRECISION):
    print('>>> Input matrix:')
    io_helper.print_matrix(coefficients, values)

    if not make_matrix_diagonal_dominance(coefficients, values):
        print("Couldn't make matrix diagonal dominant")
        return

    print('>>> Matrix after reordering:')
    io_helper.print_matrix(coefficients, values)

    n = len(coefficients)
    x = [0 for _ in range(n)]

    for i in range(1, LIMIT + 1):
        x_new = seidel_iteration(coefficients, x, values)
        if converges(x, x_new, epsilon):
            print('>>> Solution:')
            io_helper.print_x_values(x_new, precision)
            print('>>> Iterations:', i)
            print('>>> Errors:')
            io_helper.print_errors(x, x_new)
            break

        x = x_new
    else:
        print("Couldn't compute :(\nProbably diverges")


if __name__ == '__main__':
    args = sys.argv
    argc = len(args)
    if argc < 2:
        print(
            '''
            To few arguments. Usage:
            python main.py [input, file[, filename], epsilon?, precision?]
            '''
        )
        sys.exit(1)

    if args[1] not in ('input', 'file'):
        print('required data source: input or file')
        sys.exit(1)

    current_index = 2
    read_data = None
    if args[1] == 'file':
        filename = args[current_index]
        read_data = lambda: io_helper.read_data_from_file(filename)
        current_index += 1
    else:
        read_data = io_helper.read_data_from_console

    epsilon = EPSILON if argc <= current_index else float(args[current_index])
    current_index += 1
    precision = PRECISION if argc <= current_index else int(args[current_index])

    coefficients, values = read_data()
    solve(coefficients, values, epsilon, precision)
