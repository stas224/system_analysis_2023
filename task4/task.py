from collections import defaultdict
from functools import reduce
from math import log2


def task() -> list:
    counts_ab, counts_a, counts_b = defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(1, 7):
        for j in range(1, 7):
            s, p = i + j, i * j
            counts_ab[(s, p)] += 1
            counts_a[s] += 1
            counts_b[p] += 1

    calc_chance = lambda mass: {key: (value / 36) for key, value in mass.items()}
    chance_ab = calc_chance(counts_ab)
    chance_a = calc_chance(counts_a)
    chance_b = calc_chance(counts_b)

    calc_entropy = lambda mass: reduce(lambda e, chance: e - chance * log2(chance), mass.values(), 0)
    entropy_ab = calc_entropy(chance_ab)
    entropy_a = calc_entropy(chance_a)
    entropy_b = calc_entropy(chance_b)

    entropy_b_conn_a = entropy_ab - entropy_a
    information_a_about_b = entropy_b - entropy_b_conn_a

    ans_round = lambda e: round(e, 2)
    return [ans_round(i) for i in (entropy_ab, entropy_a, entropy_b, entropy_b_conn_a, information_a_about_b)]
