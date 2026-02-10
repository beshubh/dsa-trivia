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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        q = deque[TreeNode]()
        q.append(root)
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            node.left, node.right = node.right, node.left
        return root


class TestInvert(unittest.TestCase):
    def setUp(self):
        self._runner = Solution()

    def test_invert(self):
        tree = TreeNode(value=1, left=TreeNode(2), right=TreeNode(3))
        tree = self._runner.invertTree(tree)
        assert tree is not None
        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.right.value, 2)

    def test_none(self):
        tree = None
        tree = self._runner.invertTree(tree)
        self.assertIsNone(tree)

    def test_one_node(self):
        tree = TreeNode(value=1)
        tree = self._runner.invertTree(tree)
        assert tree is not None
        self.assertEqual(tree.value, 1)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_only_left(self):
        tree = TreeNode(value=1, left=TreeNode(value=2))
        tree = self._runner.invertTree(tree)
        assert tree is not None
        self.assertEqual(tree.value, 1)
        self.assertIsNone(tree.left)

        self.assertEqual(tree.right.value, 2)


if __name__ == '__main__':
    unittest.main()
