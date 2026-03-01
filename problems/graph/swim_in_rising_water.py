from heapq import heappop, heappush
from typing import List

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
INF = float('inf')

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        return dijkstra(grid)

def dijkstra(grid: list[list[int]]) -> int:
    N = len(grid)
    pq = [(grid[0][0], 0, 0)]
    dist = {}
    for r in range(N):
        for c in range(N):
            dist[(r, c)] = INF
    dist[(0, 0)] = grid[0][0]

    while pq:
        cost, r, c = heappop(pq)
        if dist[(r, c)] < cost:
            continue
        if r == N - 1 and c == N - 1:
            return cost
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = max(cost, grid[nr][nc])
                if new_cost < dist[(nr, nc)]:
                    dist[(nr, nc)] = new_cost
                    heappush(pq, (new_cost, nr, nc))
    return -1
