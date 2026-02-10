from __future__ import annotations

import unittest
from typing import Any, Optional

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(tree: Optional[TreeNode]) -> int:
            if tree is None:
                return 0

            return 1 + max(depth(tree.left), depth(tree.right))

        return depth(root)
