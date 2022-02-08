import io_helper
import sys


LIMIT = 5000


def is_diagonal_dominant(matrix):
    n = len(matrix)
    any_greater = False
    for i in range(n):
        diag_elem = matrix[i][i]
        rest_row_sum = sum(matrix[i][j] for j in range(n) if i != j)
        if diag_elem < rest_row_sum:
            return False

        if diag_elem > rest_row_sum:
            any_greater = True

    return any_greater


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


def get_delta(coefficients, vars, real_value):
    res = sum([coefficients[i] * vars[i] for i in range(len(vars))])
    return abs(res - real_value)


def solve(coefficients, values, epsilon):
    if not is_diagonal_dominant(coefficients):
        print('Matrix is not diagonal dominant')
        return

    n = len(coefficients)
    x = [0 for _ in range(n)]

    for i in range(LIMIT):
        x_new = seidel_iteration(coefficients, x, values)
        if converges(x, x_new, epsilon):
            print(*x_new)
            break

        x = x_new
    else:
        print("Couldn't compute :(")


if __name__ == '__main__':
    args = sys.argv
    argc = len(args)
    if argc < 2:
        print(
            '''
            To few arguments. Usage:
            python seidel [input, file[, filename], epsilon]
            '''
        )
        sys.exit(1)

    if args[1] == 'input':
        epsilon = 1e-6 if argc <= 2 else float(args[2])
        coefficients, values = io_helper.read_data_from_console()
        solve(coefficients, values, epsilon)
    elif args[1] == 'file':
        if argc == 2:
            print('filename required')
            sys.exit(1)

        filename = args[2]
        epsilon = 1e-3 if argc <= 3 else float(args[3])
        coefficients, values = io_helper.read_data_from_file(filename)
        solve(coefficients, values, epsilon)
    else:
        print('required data source: input or file')
        sys.exit(1)
