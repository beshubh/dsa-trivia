import collections
from heapq import heappop, heappush

def prim_mst(n: int, edges: list[tuple[int, int, int]]): # undirected edges (u, v, w)
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    seen = set([0]) # start at 0
    pq = []
    for v, w in graph[0]:
        heappush(pq, (w, v))
    cost = 0
    used_nodes = 1

    while pq and used_nodes < n:
        w, v = heappop(pq)
        if v in seen:
            continue
        seen.add(v)
        used_nodes += 1
        for neiv, neiw in graph[v]:
            if neiv not in seen:
                heappush(pq, (neiw, neiv))
    return cost if used_nodes == n else -1
