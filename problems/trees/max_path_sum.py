from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -10000

        def max_sum_path(root) -> int:
            nonlocal global_max
            if root is None:
                return -10000
            left, right = max_sum_path(root.left), max_sum_path(root.right)
            # there will 4 candidates
            # either just the root.
            # or root + left + right
            # or root + left only
            # or root + right only
            max_sum = max(root.val, root.val + left, root.val + right, root.val + left + right)
            global_max = max(global_max, max_sum)
            # candidates for parent can just be either root alone, or root either with left or with right not both because that would not be a path
            return max(root.val, root.val + left, root.val + right)

        max_sum_path(root)
        return global_max
