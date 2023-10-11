#!/bin/python

from collections import defaultdict
import csv


def find_down(root: int, children: dict, data: dict):
    stack = [root]

    while stack:
        cur_node = stack.pop()

        for child in children[cur_node]:
            data[child]['grandparents'] |= data[cur_node]['parents'] | data[cur_node]['grandparents']
            data[child]['brothers'] |= data[cur_node]['children'] - {child, }

            stack.append(child)


def find_up(leaves: tuple, parents: dict, data: dict):
    stack = list(leaves)

    while stack:
        cur_node = stack.pop()

        for parent in parents[cur_node]:
            data[parent]['grandsons'] |= data[cur_node]['children'] | data[cur_node]['grandsons']

            if parent not in stack:
                stack.append(parent)


def create_adjacency_lists(csv_str: str):
    children = defaultdict(list)
    parents = defaultdict(list)

    reader = csv.reader(csv_str.splitlines(), delimiter=',')

    for line in reader:
        if not line:
            continue

        a, b = line
        children[a].append(b)
        parents[b].append(a)

        if a not in parents:
            parents[a] = []

        if b not in children:
            children[b] = []

    return children, parents


def create_csv_str(data):
    fields = ('children',
              'parents',
              'grandsons',
              'grandparents',
              'brothers')

    csv_str = '\n'.join([
        ','.join([str(len(data[node][field])) for field in fields])
        for node in sorted(data)
    ]) + '\n'

    return csv_str


def task(csv_str: str):
    children, parents = create_adjacency_lists(csv_str)

    root = tuple(filter(lambda key: not parents[key], parents))[0]
    leaves = tuple(filter(lambda key: not children[key], children))

    certain_ans = {key: {'children': set(children[key]),
                         'parents': set(parents[key]),
                         'grandsons': set(),
                         'grandparents': set(),
                         'brothers': set()}
                   for key in parents}

    find_down(root, children, certain_ans)
    find_up(leaves, parents, certain_ans)

    csv_str = create_csv_str(certain_ans)
    return csv_str


if __name__ == "__main__":
    csv_string = input('enter csv-string: ')
    ans = task(csv_string)
    print(repr(ans))
