from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        traversal = []

        def inorder(tree):
            if tree is None:
                return
            inorder(tree.left)
            traversal.append(tree.val)
            inorder(tree.right)

        inorder(root)
        print('traversal', traversal)
        for i in range(1, len(traversal)):
            if traversal[i] > traversal[i - 1]:
                continue
            else:
                return False
        return True
