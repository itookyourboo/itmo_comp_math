import io_helper
import sys


def seidel(coefficients, vars, values):
    n = len(coefficients)

    for i in range(n):
        d = values[i]
        for j in range(n):
            if i != j:
                d -= coefficients[i][j] * vars[j]
        vars[i] = d / coefficients[i][i]

    return vars


def get_delta(coefficients, vars, real_value):
    res = sum([coefficients[i] * vars[i] for i in range(len(vars))])
    return abs(res - real_value)


LIMIT = 5000


def solve(coefficients, values, epsilon):
    n = len(coefficients)
    x = [0 for _ in range(n)]

    for i in range(LIMIT):
        x = seidel(coefficients, x, values)
        if get_delta(coefficients[0], x, values[0]) < epsilon:
            print(x)
            break
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
