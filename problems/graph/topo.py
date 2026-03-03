from collections import deque, defaultdict


def topo_sort(n: int, edges: list[tuple[int, int]]):
    g = defaultdict(list)
    indedgree = defaultdict(int)
    for u, v in edges:
        g[u].append(v)
        indedgree[v] += 1

    q = deque([x for x in range(n) if indedgree[x] == 0])
    topo_order = []
    while q:
        u = q.pop()
        topo_order.append(u)
        for v in g[u]:
            indedgree[v] -= 1
            if indedgree[v] == 0:
                q.appendleft(v)

    return topo_order if len(topo_order) == n else []
