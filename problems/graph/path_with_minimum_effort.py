from typing import List
from collections import defaultdict
from heapq import heappop, heappush



INF = float('inf')
NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1)
]

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        effort = defaultdict(lambda: INF)
        pq = [(0, 0, 0)]
        N, C = len(heights), len(heights[0])
        while pq:
            e, r, c = heappop(pq)
            if e > effort[(r, c)]:
                continue
            if r == N - 1 and c == C - 1:
                return e
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < C:
                    ne = max(abs(heights[r][c] - heights[nr][nc]), e)
                    if ne < effort[(nr, nc)]:
                        effort[(nr, nc)] =ne
                        heappush(pq, (ne, nr, nc))
        return 0
