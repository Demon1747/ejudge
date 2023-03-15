# Copyright 2022 Stepanov Dmitriy
# Task B module 2 -- splayTree

from collections import deque


class TreeError(Exception):
    pass


class SplayTree:
    # Node class
    class _Node:
        # Node constructor
        def __init__(self, key, value, parent=None):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

        # Some check functions
        def is_right_child(self):
            return self == self.parent.right

        def is_left_child(self):
            return self == self.parent.left

        # Printing node
        def __str__(self):
            if self.parent is None:
                return f"[{self.key} {self.value}]"
            else:
                return f"[{self.key} {self.value} {self.parent.key}]"

    # Splay tree constructor
    def __init__(self):
        self._root = None

    # Creating string from tree
    def __str__(self):
        if self._root is None:
            return "_"
        queue = deque()
        queue.append([1, self._root])
        border = 2
        prev_node_num = 0
        res_str = list()
        line = list()
        while len(queue) > 0:
            tmp = queue.popleft()
            node_num = tmp[0]
            cur_node = tmp[1]
            if cur_node.left is not None:
                queue.append([2 * node_num, cur_node.left])
            if cur_node.right is not None:
                queue.append([2 * node_num + 1, cur_node.right])
            if node_num >= border:
                line.extend('_' * (border - 1 - prev_node_num))
                res_str.append(' '.join(line))
                line.clear()
                border *= 2
            if prev_node_num < (border // 2) - 1:
                prev_node_num = (border // 2) - 1  # Crutch
            if node_num > prev_node_num + 1:
                line.extend('_' * (node_num - 1 - prev_node_num))
            line.append(str(cur_node))
            prev_node_num = node_num
            if len(queue) == 0:
                line.extend('_' * (border - 1 - prev_node_num))
                res_str.append(' '.join(line))
                break
        return '\n'.join(res_str)

    # Adding node into tree
    def add(self, key, value):
        cur_node = self._root
        cur_parent = None
        while cur_node is not None:
            cur_parent = cur_node
            if key < cur_node.key:
                cur_node = cur_node.left
            elif key > cur_node.key:
                cur_node = cur_node.right
            else:
                self._splay(cur_node)
                raise TreeError
        cur_node = self._Node(key, value, cur_parent)
        if cur_parent is None:
            self._root = cur_node
        elif key <= cur_parent.key:
            cur_parent.left = cur_node
        else:
            cur_parent.right = cur_node
        self._splay(cur_node)

    # Setting a value for a given key
    def set(self, key, value):
        if self.search(key) is None:
            raise TreeError
        self._root.value = value

    # Deleting node with given key
    def delete(self, key):
        if self.search(key) is None:
            raise TreeError
        r_subtree = self._root.right  # Making right subtree
        self._root = self._root.left  # Making left subtree
        if r_subtree is None and self._root is None:
            self._root = None
        elif self._root is not None and r_subtree is None:
            self._root.parent = None
        elif r_subtree is not None and self._root is None:
            self._root = r_subtree
            self._root.parent = None
        else:
            self._root.parent = None
            self.max()
            self._root.right = r_subtree
            if r_subtree is not None:
                r_subtree.parent = self._root

    # Searching for node with given key
    def search(self, key):
        cur_node = self._root
        cur_parent = None
        while cur_node is not None and cur_node.key != key:
            cur_parent = cur_node
            if key < cur_node.key:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        if cur_node is not None:
            self._splay(cur_node)
            return self._root.value
        elif cur_parent is not None:
            self._splay(cur_parent)
        return None

    # Min
    def min(self):
        cur_node = self._root
        while cur_node is not None and cur_node.left is not None:
            cur_node = cur_node.left
        if cur_node is None:
            raise TreeError
        self._splay(cur_node)
        return self._root.key, self._root.value

    # Max
    def max(self):
        cur_node = self._root
        while cur_node is not None and cur_node.right is not None:
            cur_node = cur_node.right
        if cur_node is None:
            raise TreeError
        self._splay(cur_node)
        return self._root.key, self._root.value

    # Auxiliary functions ########################################

    # Splay
    def _splay(self, node):
        while self._root != node:
            if node.parent == self._root:
                # Zig
                if node.is_left_child():
                    self._right_rotation(node.parent)
                else:
                    self._left_rotation(node.parent)
            else:
                if node.is_left_child() and node.parent.is_left_child():
                    # ZigZig
                    self._right_rotation(node.parent.parent)
                    self._right_rotation(node.parent)
                elif node.is_right_child() and node.parent.is_right_child():
                    # ZigZig
                    self._left_rotation(node.parent.parent)
                    self._left_rotation(node.parent)
                elif node.is_left_child() and node.parent.is_right_child:
                    # ZigZag
                    self._right_rotation(node.parent)
                    self._left_rotation(node.parent)
                else:
                    # ZigZag
                    self._left_rotation(node.parent)
                    self._right_rotation(node.parent)

    # Right rotation of node
    def _right_rotation(self, node):
        godfather = node.parent
        if godfather is None:
            self._root = node.left
        elif node.is_left_child():
            godfather.left = node.left
        else:
            godfather.right = node.left

        node.parent = node.left
        node.left = node.left.right
        if node.left is not None:
            node.left.parent = node

        node.parent.right = node
        node.parent.parent = godfather

    # Left rotation of node
    def _left_rotation(self, node):
        godfather = node.parent
        if godfather is None:
            self._root = node.right
        elif node.is_left_child():
            godfather.left = node.right
        else:
            godfather.right = node.right

        node.parent = node.right

        node.right = node.right.left
        if node.right is not None:
            node.right.parent = node

        node.parent.left = node
        node.parent.parent = godfather


if __name__ == "__main__":
    splay_tree = SplayTree()
    while True:
        try:
            input_text = input()
            args = input_text.split(' ')
            if not len(input_text):
                continue

            if len(args) == 3:
                if args[0] == "add":
                    splay_tree.add(int(args[1]), args[2])  # add K V
                elif args[0] == "set":
                    splay_tree.set(int(args[1]), args[2])  # set K V
                else:
                    print("error")
            elif len(args) == 2:
                if args[0] == "delete":
                    splay_tree.delete(int(args[1]))  # delete K
                elif args[0] == "search":
                    res = splay_tree.search(int(args[1]))  # search K
                    if res is None:
                        print(0)
                    else:
                        print(1, res)
                else:
                    print("error")
            elif len(args) == 1:
                if args[0] == "min":
                    print(*splay_tree.min())  # min
                elif args[0] == "max":
                    print(*splay_tree.max())  # max
                elif args[0] == "print":
                    print(str(splay_tree))  # print
                else:
                    print("error")
            else:
                print("error")
        except TreeError:
            print("error")
            continue
        except EOFError:
            break
