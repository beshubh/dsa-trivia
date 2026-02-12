from __future__ import annotations

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(tree):
            if tree is None:
                return [True, 0]

            left, right = dfs(tree.left), dfs(tree.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)
