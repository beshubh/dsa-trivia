from __future__ import annotations

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def get_ancestors(tree, t):
            res = []
            while tree:
                if tree.val == t.val:
                    res.append(t)
                    return res

                res.append(tree)
                if t.val < tree.val:
                    tree = tree.left
                else:
                    tree = tree.right
            return res

        def lca(root, p, q):
            p_anc = get_ancestors(root, p)
            q_anc = get_ancestors(root, q)

            p_itr, q_itr = iter(p_anc), iter(q_anc)
            common = None
            while True:
                pva = next(p_itr, None)
                qva = next(q_itr, None)
                if pva is not None and qva is not None and pva.val == qva.val:
                    common = pva
                else:
                    break

            return common.val if common else None

        return lca(root, p, q)
