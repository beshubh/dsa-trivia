from __future__ import annotations

import unittest
from typing import Any


class Node:
    def __init__(self, value: Any = None, next: Node | None = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        node = Node()
        self._head = node
        self._tail = node

    def add_to_end(self, node: Node) -> None:
        self._tail.next = node
        self._tail = node

    def add_to_head(self, node: Node) -> None:
        node.next = self._head.next
        self._head.next = node

    def __str__(self) -> str:
        res = []
        node = self._head
        while node is not None:
            res.append(f'{node.value} ->')
            node = node.next
        return ''.join(res)


class TestLinkedList(unittest.TestCase):
    def test_basic(self):
        llist = LinkedList()

        llist.add_to_end(Node(10))
        llist.add_to_end(Node(5))
        print(llist)


if __name__ == "__main__":
    unittest.main()
