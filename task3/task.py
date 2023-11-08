import csv
import math


def get_data(csv_str: str):
    reader = csv.reader(csv_str.splitlines(), delimiter=',')
    data = list(reader)
    return data, len(data)


def get_entropy_cell(cell, count):
    if cell != '0':
        digit = float(cell) / (count - 1)
        return -digit * math.log2(digit)
    return 0


def task(csv_str: str):
    data, count = get_data(csv_str)
    entropy_ = 0

    for row in data:
        for cell in row:
            entropy_ += get_entropy_cell(cell, count)

    return round(entropy_, 1)


if __name__ == '__main__':
    csv_string = '1,0,4,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,2,1\n0,1,0,2,1\n'
    csv_string2 = '1,0,2,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,1,1\n0,1,0,1,1\n'
    entropy = task(csv_string)
    print(entropy)
