from __future__ import annotations

from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, key: Any, value: Any, prev: Node | None = None, next: Node | None = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self, capacity: int):
        self._head, self._tail = Node('dumh', 0), Node('dumt', 0)
        self._head.next, self._tail.prev = self._tail, self._head
        self._capacity = capacity
        self._size = 0

    def _remove_from_list(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if prev_node is None or next_node is None:
            # impossible scenario
            return
        prev_node.next, next_node.prev = next_node, prev_node
        self._size -= 1

    def move_to_head(self, node: Node):
        self._remove_from_list(node)
        self.add_to_head(node)

    def pop_tail(self) -> Node | None:
        last_node = self._tail.prev
        if last_node is self._head:
            # we don't have element in the list
            return None
        self._remove_from_list(last_node)
        return last_node

    def add_to_head(self, node: Node):
        self._size += 1
        if self._head.next is None:
            self._head.next = node
            self._tail.prev = node
        else:
            node.next, node.prev = self._head.next, self._head
            self._head.next.prev = node
            self._head.next = node

    def size(self):
        return self._size


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._list = DLinkedList(capacity)
        self._cache = {}

    def get(self, key: int) -> int:
        node: Node | None = self._cache.get(key, None)
        if node is None:
            return -1
        self._list.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node: Node = self._cache[key]
            node.value = value
            self._list.move_to_head(node)
        else:
            node = Node(key=key, value=value)
            self._list.add_to_head(node)
            self._cache[key] = node
        while self._list.size() > self._capacity:
            # remove one from tail
            node: Node | None = self._list.pop_tail()

            if node and node.key in self._cache:
                del self._cache[node.key]
