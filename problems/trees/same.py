from __future__ import annotations
from collections import deque

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(tree1, tree2):
            q1, q2 = deque[TreeNode](), deque[TreeNode]()
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            q1.append(tree1)
            q2.append(tree2)
            while q1 and q2:
                node1, node2 = q1.pop(), q2.pop()
                if node1.value != node2.value:
                    return False
                if node1.left:
                    q1.append(node1.left)
                if node1.right:
                    q1.append(node1.right)

                if node2.left:
                    q2.append(node2.left)
                if node2.right:
                    q2.append(node2.right)
            return True

        return bfs(p, q)


class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q or p.value != q.value:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
