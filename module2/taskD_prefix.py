# # Copyright 2022 Stepanov Dmitriy
# # Task C module 2 -- prefixTree
#
#
# class RadixTree:
#     # Tree node class
#     class _Node:
#         def __init__(self, in_value=None, in_children=None, in_end=True):
#             self.value = in_value
#             if in_children is None:
#                 self.children = (in_children if in_children else set())
#             self._children = in_children
#             self.end = in_end
#
#     # Constructor
#     def __init__(self):
#         self._node = None
#
#     def add_word(self, input_word):
#         if self._node is None:
#             self._node = self._Node(input_word, {}, True)
#             return
#         cur_node = self._node
#         if input_word[0] not in self._node.children:
#
#
#     def _common_prefix(self, str1, str2):
#         i = 0
#         for _ in range(min(len(str1), len(str2))):
#             if str1[i] != str2[i]:
#                 break
#             i += 1
#         return str1[:i]
#
#     def _dl_distance(self, str1, str2):
#         n, m = len(str1), len(str2)
#         if n > m:
#             str1, str2 = str2, str1
#             n, m = m, n
#
#         table = [[i + j for i in range(n + 1)] for j in range(m + 1)]
#
# # Parser (main)
# if __name__ == "__main__":
#     trie = Trie()
#     dict_size = int(input())
#     for _ in range(dict_size):
#         Trie.add_word(input()
#
#     while True:
#         try:
#             line = input().lower()
#             if len(line) == 0:
#                 continue
#
#             Trie.check(line)
#         except EOFError:
#             break
