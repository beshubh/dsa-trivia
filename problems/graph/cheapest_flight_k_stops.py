import collections
from heapq import heappop, heappush
from typing import List


INF = float('inf')

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        dist = {}
        for u, v, p in flights:
            graph[u].append((v, p))
        dist[(src, 0)] = 0
        pq = [(0, src, 0)] # cost, node, flights_used
        while pq:
            cost, current, flights_used = heappop(pq)
            if dist.get((current, flights_used), INF) < cost:
                continue
            if current == dst and flights_used <= k + 1:
                return cost
            if flights_used == k + 1:
                continue
            for v, np in graph.get(current, []):
                ncost = np + cost
                if dist.get((v, flights_used + 1), INF) > ncost:
                    dist[(v, flights_used + 1)] = ncost
                    heappush(pq, (ncost, v, flights_used + 1))
        return -1
