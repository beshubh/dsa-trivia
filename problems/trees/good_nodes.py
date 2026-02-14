from __future__ import annotations

from typing import Any
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(tree, max_encountered):
            nonlocal ans
            if tree is None:
                return
            if tree.val >= max_encountered:
                ans += 1
                max_encountered = tree.val

            dfs(tree.left, max_encountered)
            dfs(tree.right, max_encountered)

        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return ans + 1
