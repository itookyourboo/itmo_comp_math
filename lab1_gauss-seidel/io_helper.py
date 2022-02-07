def separate_coefficients_and_value(array):
    *coefficients, value = array
    return coefficients, value


def get_rows_by_first_line(line):
    return len(line.split()) - 1


def read_data_from_lines(lines):
    coefficients_1, value_1 = separate_coefficients_and_value(list(map(int, lines[0].split())))
    coefficients, values = [coefficients_1], [value_1]
    for i in range(1, len(coefficients[0])):
        *row_coefficients, row_value = list(map(int, lines[i].split()))
        coefficients.append(row_coefficients)
        values.append(row_value)

    return coefficients, values


def read_data_from_console():
    lines = [input()]
    for i in range(1, get_rows_by_first_line(lines[0])):
        lines.append(input())

    return read_data_from_lines(lines)


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = list(map(lambda x: x.rstrip('\n'), file.readlines()))
        return read_data_from_lines(lines)
