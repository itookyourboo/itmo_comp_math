import numpy as np
from prettytable import PrettyTable


def format_float(x):
    if isinstance(x, np.bool_):
        return x
    return f'{x:.3f}'


def get_result_table(result):
    tt = PrettyTable(result.header)
    data = [(n, *map(format_float, floats)) for n, *floats in result.data]
    tt.add_rows(data)
    return tt


def get_root_table(data):
    tt = PrettyTable(['x1', 'x2', 'Единственный корень?'])
    tt.add_rows([list(map(format_float, floats)) for floats in data])
    return tt


def get_intervals_table(intervals):
    tt = PrettyTable(['x', 'f(x)', 'f\'(x)'])
    tt.add_rows([list(map(format_float, floats)) for floats in intervals])
    return tt


def output(content, file=None):
    if file:
        file.write(str(content) + '\n')
    else:
        print(content)


def def_input(prompt, def_value=None):
    v = input(f'{prompt} ({def_value}): ') if def_value is not None else input(f'{prompt}: ')
    return v if v.strip() else def_value
