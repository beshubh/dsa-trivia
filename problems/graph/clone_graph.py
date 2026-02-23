import collections
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def bfs(node):
            if node is None:
                return None
            q = collections.deque([node])
            clones = {node: Node(node.val)}

            while q:
                current  = q.pop()
                for nei in current.neighbors:
                    if nei not in clones:
                        q.appendleft(nei)
                        clones[nei] = Node(nei.val)
                    clones[current].neighbors.append(clones[nei])
            return clones[node]
        return bfs(node)
