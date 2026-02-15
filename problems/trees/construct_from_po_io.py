from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def inner(preorder, inorder):
            if not preorder:
                return None
            root = preorder[0]
            print('root: ', root)
            print('preorder: ', preorder, '\ninorder: ', inorder)
            try:
                partition = inorder.index(root)
            except ValueError:
                return None
            left_part, right_part = inorder[:partition], inorder[partition + 1 :]
            print('left: ', left_part, '\nright: ', right_part)
            tree = TreeNode(
                val=root,
                left=inner(preorder[1 : partition + 1], left_part),
                right=inner(preorder[partition + 1 :], right_part),
            )
            return tree

        return inner(preorder, inorder)
