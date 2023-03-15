# Copyright 2022 Stepanov Dmitriy
# Task C module 3 -- Knapsack solver

from math import floor, gcd


class Item:
    def __init__(self, w, c, i):
        self.w = w  # Item weight
        self.v = c  # Item cost
        self.i = i  # Item index


# Algorithm itself
def knapsack_approximate_task_destroyer(e, w_max, items):
    # Throwing away useless items and getting the max cost
    scaled_items = list()
    v_max = 0

    for item in items:
        if item.w <= w_max and item.v != 0:
            scaled_items.append(Item(item.w, item.v, item.i))
            if item.v > v_max:
                v_max = item.v

    n = len(scaled_items)

    if n == 0:
        return 0, 0, set()

    # Getting scaled costs
    if e != 0:
        if e < 0.005:  # I am so sorry:(
            e = 0.005
        coef = n / (v_max * e)
        for i in range(len(scaled_items)):
            scaled_items[i].v = floor(scaled_items[i].v * coef)

    v_sum = 0
    for i in scaled_items:
        v_sum += i.v
    res_j = 0

    # Creating memorisation table
    mem_table = [[0] * (v_sum + 1) for _ in range(n + 1)]
    for j in range(1, v_sum + 1):
        mem_table[0][j] = w_max * n  # == +Infinity

    for i in range(1, n + 1):
        for j in range(0, v_sum + 1):
            if j >= scaled_items[i - 1].v:
                mem_table[i][j] = min(mem_table[i - 1][j],
                                      scaled_items[i - 1].w + mem_table[i - 1][j - scaled_items[i - 1].v])
            else:
                mem_table[i][j] = min(mem_table[i - 1][j], scaled_items[i - 1].w)

    for j in range(v_sum, 0, -1):
        if mem_table[n][j] <= w_max:
            res_j = j
            break

    res_cost = 0
    diag_j = res_j
    indexes = set()
    for i in range(n, 0, -1):
        if mem_table[i][diag_j] - mem_table[i - 1][diag_j - scaled_items[i - 1].v] == scaled_items[i - 1].w:
            indexes.add(scaled_items[i - 1].i)
            res_cost += items[scaled_items[i - 1].i - 1].v
            diag_j -= scaled_items[i - 1].v
        if diag_j <= 0:
            break

    return mem_table[n][res_j], res_cost, indexes


# Parser (main)
if __name__ == "__main__":
    in_e = None  # Approximation coefficient
    in_w_max = None  # Max weight
    line = ''
    try:
        while len(line) == 0:
            line = input()
        in_e = float(line)
        line = ''
        while len(line) == 0:
            line = input()
        in_w_max = int(line)
    except EOFError:
        quit()

    index = 1
    items_list = list()  # List of input items
    while True:
        try:
            line = input()
            if len(line) == 0:
                continue
            args = line.split()
            item_w, item_v = int(args[0]), int(args[1])
            items_list.append(Item(item_w, item_v, index))
            index += 1

        except EOFError:
            break

    # Press big red button
    res_w, res_c, indexes = knapsack_approximate_task_destroyer(in_e, in_w_max, items_list)
    print(res_w, res_c)
    for i in indexes:
        print(i)
