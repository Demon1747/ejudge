# Copyright 2022 Stepanov Dmitriy
# Task B module 3 -- Bloom filter

from math import log, sqrt, ceil


class BloomFilter:

    # Bit array
    class BitArray:
        # Bit array constructor
        def __init__(self, m):
            self._array = bytearray(ceil(m / 8))

            # Array size
            self._size = m

        # Set 1
        def set(self, k):
            byte_pos = k // 8
            bit_pos = k % 8
            self._array[byte_pos] = self._array[byte_pos] | (1 << bit_pos)

        # Get item
        def __getitem__(self, index):
            byte_pos = index // 8
            bit_pos = index % 8
            return int(self._array[byte_pos] & (1 << bit_pos) == 1 << bit_pos)

        # Get string
        def __str__(self):
            res = list('0' * self._size)
            for i in range(self._size):
                res[i] = str(self[i])
            return "".join(res)

    # Bloom filter constructor
    def __init__(self, n, P):
        # Checks log
        if round(-log(P, 2)) == 0:
            raise ValueError

        # Struct size
        self._m = round(-n * log(P, 2) / log(2))

        # Number of hash functions
        self._k = round(-log(P, 2))

        # 31-st Mersenne number
        self._M = 2 ** 31 - 1

        # First h prime numbers
        self._primes = self._n_primes(self._k)

        # Bit array
        self._bitArray = self.BitArray(self._m)

    # Returns list with first n prime numbers
    def _n_primes(self, n):

        primes = [2, 3]
        if n < 3:
            return primes[:n]

        # Some optimisations included
        i = 3
        while len(primes) < n:
            i += 2
            flag = True
            for j in range(1, len(primes)):
                if sqrt(i) < primes[j]:
                    break
                if i % primes[j] == 0 or sqrt(i) < primes[j]:
                    flag = False
                    break
            if flag:
                primes.append(i)
        return primes

    # Hash function with key x and i number
    def _hash(self, x, i):
        return (((i + 1) * x + self._primes[i]) % self._M) % self._m

    def m(self):
        return self._m

    def k(self):
        return self._k

    # Adds K key in filter
    def add(self, K):
        for i in range(self._k):
            hash_i = self._hash(K, i)
            self._bitArray.set(hash_i)

    # Searches K key in filter
    def search(self, K):
        for i in range(self._k):
            hash_i = self._hash(K, i)
            if not self._bitArray[hash_i]: # if bit == 0
                return 0
        return 1

    # Prints bit array
    def print(self):
        return str(self._bitArray)


if __name__ == "__main__":
    while True:
        try:
            in_str = input()
            args = in_str.split(' ')
            if len(in_str) == 0:
                continue
            if args[0] == "set" and len(args) == 3 and int(args[1]) > 0 and 0 < float(args[2]) < 1:
                n = int(args[1])
                P = float(args[2])
                try:
                    bloom_filter = BloomFilter(n, P)
                except ValueError:
                    print("error")
                    continue

                print(bloom_filter.m(), bloom_filter.k())
                break
            else:
                print("error")
        except EOFError:
            break

    while True:
        try:
            in_str = input()
            args = in_str.split(' ')
            if len(in_str) == 0:
                continue

            if len(args) == 2 and args[0] == "add":
                bloom_filter.add(int(args[1]))  # add K
            elif len(args) == 2 and args[0] == "search":
                res = bloom_filter.search(int(args[1]))  # search K
                print(res)
            elif len(args) == 1 and args[0] == "print":  # print
                print(bloom_filter.print())
            else:
                print("error")

        except EOFError:
            break
