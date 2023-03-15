# Copyright 2022 Stepanov Dmitriy
# Task C module 2 -- minHeap

class MinHeap:
    # Min heap constructor
    def __init__(self):
        # Heap itself -- consists of [key, value] elements (list type)
        self._heap = list()

        # Hash table -- map with { key: index in heap } elements
        self._map = dict()

    # Adding "V" value in heap element with "K" key
    def add(self, key, value):
        if key in self._map:
            print("error")
            return
        self._map[key] = len(self._heap)
        self._heap.append([key, value])
        self._sift_up(len(self._heap) - 1)

    # Setting "V" value in heap element with "K" key
    def set(self, key, value):
        if key not in self._map:
            print("error")
        else:
            self._heap[self._map[key]][1] = value

    # Deleting element with "K" key from heap
    def delete(self, key):
        if key not in self._map or len(self._heap) == 0:
            print("error")
            return
        last_index = len(self._heap) - 1
        index = self._map[key]
        self._swap(index, last_index)
        self._heap.pop()
        del self._map[key]

        if 0 < index < len(self._heap) and self._heap[index][0] < self._heap[(index - 1) // 2][0]:
            self._sift_up(index)
        else:
            self._heapify(index)

    # Removing the top of the heap
    def extract(self):
        if len(self._heap) == 0:
            print("error")
            return
        print(self._heap[0][0], self._heap[0][1])
        self._swap(0, len(self._heap) - 1)
        del self._map[self._heap[-1][0]]
        self._heap.pop()
        self._heapify(0)

    # Searching element with "K" key in heap
    def search(self, key):
        if key not in self._map:
            print(0)
        else:
            index = self._map[key]
            print(1, index, self._heap[index][1])

    # Returning the top of the heap
    def min(self):
        if len(self._heap) == 0:
            print("error")
        else:
            print(self._heap[0][0], 0, self._heap[0][1])

    # Returning the max element of the heap
    def max(self):
        if len(self._heap) == 0:
            print("error")
            return
        key = max(self._map.keys())
        index = self._map[key]
        print(key, index, self._heap[index][1])

    # Printing heap
    def print(self):
        if len(self._heap) == 0:
            print('_')
            return
        print(f"[{self._heap[0][0]} {self._heap[0][1]}]")
        mult = 2
        border = 0
        i = 1
        while border + 1 < len(self._heap):
            border += mult
            mult *= 2
            while i <= border:
                if i < len(self._heap):
                    if i != border:
                        print(f"[{self._heap[i][0]} {self._heap[i][1]} {self._heap[(i - 1) // 2][0]}]", end=' ')
                    else:
                        print(f"[{self._heap[i][0]} {self._heap[i][1]} {self._heap[(i - 1) // 2][0]}]")
                else:
                    if i != border:
                        print('_', end=' ')
                    else:
                        print('_')
                i += 1

    # Heapify (or sift_down) operation
    def _heapify(self, index):
        left_i = index * 2 + 1
        right_i = index * 2 + 2
        tmp_i = index
        if left_i < len(self._heap) and self._heap[tmp_i][0] > self._heap[left_i][0]:
            tmp_i = left_i
        if right_i < len(self._heap) and self._heap[tmp_i][0] > self._heap[right_i][0]:
            tmp_i = right_i
        if tmp_i != index:
            self._swap(tmp_i, index)
            self._heapify(tmp_i)

    # Sift-up operation
    def _sift_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self._heap[index][0] < self._heap[parent][0]:
            self._swap(index, parent)
            self._sift_up(parent)

    # Swapping heap elements
    def _swap(self, i_a, i_b):
        # Switching indexes in hash table
        self._map[self._heap[i_a][0]] = i_b
        self._map[self._heap[i_b][0]] = i_a

        # Switching elements
        self._heap[i_a], self._heap[i_b] = self._heap[i_b], self._heap[i_a]


# Entry point #################################################################

# Creating heap
min_heap = MinHeap()

# input data parser
while True:
    try:
        input_text = input()
        args = input_text.split(' ')
        if not len(input_text):
            continue

        if len(args) == 3:
            if args[0] == "add":
                min_heap.add(int(args[1]), args[2])  # add K V
            elif args[0] == "set":
                min_heap.set(int(args[1]), args[2])  # set K V
        elif len(args) == 2:
            if args[0] == "delete":
                min_heap.delete(int(args[1]))  # delete K
            elif args[0] == "search":
                min_heap.search(int(args[1]))  # search K
        elif len(args) == 1:
            if args[0] == "min":
                min_heap.min()  # min
            elif args[0] == "max":
                min_heap.max()  # max
            elif args[0] == "extract":
                min_heap.extract()  # extract
            elif args[0] == "print":
                min_heap.print()  # print
        else:
            print("error")

    except EOFError:
        break
