import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.pop()
                level.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            res.append(level[-1])
        return res
