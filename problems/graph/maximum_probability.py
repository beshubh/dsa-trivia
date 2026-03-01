
from typing import List
from heapq import heappop, heappush
from collections import defaultdict


INF = float('inf')

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = {x: [] for x in range(n)}
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = defaultdict(lambda: 0.0)
        pq = [(-1, start_node)]
        prob[start_node] = 1.0

        while pq:
            p, u = heappop(pq)
            if -p > prob[u]:
                continue
            if u == end_node:
                return -p
            for v, neip in graph.get(u, []):
                np = -p * neip
                if np > prob[v]:
                    prob[v] = np
                    heappush(pq, (-np, v))
        return 0.0
