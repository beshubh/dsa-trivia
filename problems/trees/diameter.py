from __future__ import annotations

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def length(tree: Optional[TreeNode]) -> int:
            nonlocal max_dia
            if tree is None:
                return 0
            left_length, right_length = 0, 0
            if tree.left:
                left_length = 1 + length(tree.left)
            if tree.right:
                right_length = 1 + length(tree.right)
            max_dia = max(max_dia, left_length + right_length)
            return max(left_length, right_length)

        length(root)
        return max_dia


def main():
    tree = TreeNode(value=1, left=TreeNode(2), right=TreeNode(3))
    sol = Solution().diameterOfBinaryTree(tree)
    print('diameter: ', sol)


if __name__ == '__main__':
    main()
