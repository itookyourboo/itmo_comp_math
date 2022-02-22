from prettytable import PrettyTable


def format_float(x):
    return f'{x:.3f}'


def get_table(result):
    tt = PrettyTable(result.header)
    data = [(n, *map(format_float, floats)) for n, *floats in result.data]
    tt.add_rows(data)
    return tt


def output(content, file=None):
    (file.write if file else print)(str(content) + '\n')


def def_input(prompt, def_value=None):
    v = input(f'{prompt} ({def_value}): ') if def_value else input(f'{prompt}: ')
    return v if v.strip() else def_value
