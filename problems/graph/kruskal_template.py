

class DSU:

    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n + 1))
        self.rank: list[int] = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        return True


def kruskal_mst(n: int, edges: list[tuple[int, int, int]]): # edges: (u, v, w)
    edges.sort(key = lambda x: x[2])
    dsu = DSU(n)
    cost = 0
    used = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            cost += w
            used += 1
            if used == n - 1:
                return cost
    return -1 # graph not fully connected
