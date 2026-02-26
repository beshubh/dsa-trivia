
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank  = [0] * (n + 1)


    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False # a and b are already connected by some path
        # union by the rank
        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        self.parent[parent_b] = parent_a
        if self.rank[parent_a] == self.rank[parent_b]:
            self.rank[parent_a] += 1
        return True




class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
       dsu = DSU(len(edges))
       # a graph with no cycle and connected is basically a tree
       # a tree has n - 1 edges, this graph as the problem states have n edges now.
       # we can DSU of n and try to union all the edges whatever is already connected is basically the cyle edge
       for u, v in edges:
           if not dsu.union(u, v):
               return [u, v]
        raise ValueError("No solution exists")
