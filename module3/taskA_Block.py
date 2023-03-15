# Copyright 2022 Stepanov Dmitriy
# Task A module 3 -- Block

"""
Сложности
- Парсинг: O(n) по времени, O(n) по памяти
- Сортировка списка: O(n log(n)) по времени, O(n) по памяти
- Проход по списку: O(n) по времени, O(1) по памяти

Общая сложность:
O(n log(n)) по времени и O(n) по памяти
"""


def blocking_time_end(N, P, B, B_max, cur_time, req_list):
    req_list.sort()   # Используется Timsort, O(n log(n)) по времени и O(n) дополнительной памяти
    B_current = B
    unblock_time = 0
    ref_point = 0
    ctr = 0
    for i in range(len(req_list)):   # O(n) по времени, т.к. требуется всего один проход по циклу, O(1) памяти
        if req_list[i] > cur_time:
            break
        if req_list[i] < cur_time - 2 * B_max:
            continue

        if ctr == 0:
            ref_point = i
            ctr = 1
        elif req_list[i] - req_list[ref_point] <= P:
            ctr += 1
        elif req_list[i] - req_list[ref_point] > P:
            ref_point += 1

        if ctr == N:
            unblock_time = req_list[i] + B_current
            B_current *= 2
            if B_current > B_max:
                B_current = B_max
            ctr = 0

    if unblock_time < cur_time:
        return 0
    return unblock_time


# Parser (main)
if __name__ == "__main__":
    start_args = input().split()
    if len(start_args) == 0:
        quit()
    in_N = int(start_args[0])
    in_P = int(start_args[1])
    in_B = int(start_args[2])
    in_B_max = int(start_args[3])
    in_cur_t = int(start_args[4])

    requests = list()
    while True:  # O(n) по времени и O(n) памяти для хранения значений (их необходимо сортировать)
        try:
            in_data = int(input())
            requests.append(in_data)
        except EOFError:
            break

    block_reset_time = blocking_time_end(in_N, in_P, in_B, in_B_max, in_cur_t, requests)
    if block_reset_time == 0:
        print("ok")
    else:
        print(block_reset_time)
