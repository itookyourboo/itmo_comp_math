import numpy as np
import matplotlib.pyplot as plt


def read_data_from_lines(lines):
    xs = list(map(float, lines[0].split()))
    ys = list(map(float, lines[1].split()))
    return xs, ys


def read_data_from_console():
    lines = [input(), input()]
    return read_data_from_lines(lines)


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = list(map(lambda x: x.rstrip('\n'), file.readlines()))
        return read_data_from_lines(lines)


def output(s, file=None):
    if file:
        file.write(str(s) + '\n')
    else:
        print(s)


OFFSET = 5


def show_graph(xs, ys, results):
    x1, x2, y1, y2 = min(xs), max(xs), min(ys), max(ys)
    bx, by = max(abs(x1), abs(x2)) + OFFSET, max(abs(y1), abs(y2)) + OFFSET
    x = np.linspace(min(xs) - OFFSET, max(xs) + OFFSET, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.grid(True)
    plt.xlim((-bx, bx))
    plt.ylim((-by, by))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    for result in results:
        xt = x
        y = np.vectorize(result.function)
        try:
            y(x)
        except ValueError:
            xt = x[x > 0]
        finally:
            ax.plot(xt, y(xt), label=result.function_str)

    ax.plot(xs, ys, 'ro')
    plt.legend()

    plt.show()
