from functools import reduce
import json


def open_json(filename):
    with open(filename) as f:
        j = json.load(f)

    return j


def evaluate(ranjs):
    x_max = [i * len(ranjs) for i in range(1, len(ranjs[0]) + 1)]
    m = sum(x_max) / len(ranjs[0])
    d_max = reduce(lambda a, b: a + (b - m) ** 2, x_max, 0) / (len(ranjs[0]) - 1)

    ranjs_t = list(zip(*ranjs))
    x = [sum(row) for row in ranjs_t]
    d = reduce(lambda a, b: a + (b - m) ** 2, x, 0) / (len(ranjs[0]) - 1)
    candle = d / d_max
    return round(candle, 2)


def make_trans_dict(mark):
    trans = {}

    for i, elem in enumerate(mark, 1):
        if isinstance(elem, list):
            for inner_elem in elem:
                trans[inner_elem] = i
        else:
            trans[elem] = i
    reverse_trans = {i: elem for elem, i in trans.items()}

    return trans, reverse_trans


def make_conversion(marks, trans):
    positions = []

    for mark in marks:
        row = []
        for elem in mark:
            if isinstance(elem, list):
                for inner_elem in elem:
                    row.append(trans[inner_elem])
            else:
                row.append(trans[elem])
        positions.append(row)

    return positions


def task():
    filenames = ['ranj_a.json', 'ranj_b.json', 'ranj_c.json']
    marks = [open_json(filename) for filename in filenames]
    trans, reverse_trans = make_trans_dict(marks[0])
    positions = make_conversion(marks, trans)
    value = evaluate(positions)
    return value


if __name__ == "__main__":
    ans = task()
    print(ans)
