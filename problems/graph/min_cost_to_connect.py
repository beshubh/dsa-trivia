class Solution:

    def mhd(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        edges = []
        for u in points:
            for v in points:
                if u == v:
                    continue
                u = tuple(u)
                v = tuple(v)
                edges.append((u, v, self.mhd(u, v)))
        edges.sort(key = lambda x: x[2])
        dsu = DSU(points)
        used = 0
        cost = 0
        for u, v, w in edges:
            if dsu.union(u, v):
                cost += w
                used += 1
                if used == len(points) - 1:
                    return cost

        return 0


class DSU:

    def __init__(self, points: list[list[int]]) -> None:
        self.parent: dict = {tuple(x): tuple(x) for x in points}
        self.rank: dict = {tuple(x): 0 for x in points}

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        return True
