from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head

        def deep_copy_list(node: Node | None, visited: dict) -> Node | None:
            """This only works for non cyclic linked lists"""
            if node is None:
                return None

            new_node = Node(node.val, deep_copy_list(node.next, visited))
            visited[node] = new_node
            return new_node

        visited_map = {}
        copy_head = deep_copy_list(curr, visited_map)

        curr = head
        while curr:
            new_node = visited_map[curr]  # we are guranteed to always have this
            if curr.random:
                new_node.random = visited_map[curr.random]
            curr = curr.next
        return copy_head
