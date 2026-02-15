from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        po, io = [], []

        def preorder(root):
            nonlocal po
            if not root:
                po.append('nil')
                return

            po.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ','.join(po)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        po = [int(x) if x != 'nil' else None for x in data.split(',')]

        def build_tree(preorder, idx=0):
            if idx >= len(preorder):
                return [None, -1]

            if preorder[idx] is None:
                return [None, idx + 1]
            root = TreeNode(preorder[idx])
            left, next_idx = build_tree(preorder, idx + 1)
            if next_idx == -1:
                root.left = None
                root.right = None
                return [root, -1]

            right, next_idx = build_tree(preorder, next_idx)
            root.left = left
            root.right = right
            return [root, next_idx]

        return build_tree(po)[0]
