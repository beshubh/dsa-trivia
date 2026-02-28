import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        graph = {x: [] for x in range(1, n + 1)} # src -> (weight, dst)
        for u, v, w in times:
            graph[u].append((w, v))

        if k not in graph:
            return -1

        visit = set()
        def bfs_shortest(k: int) -> int:
            q = [(0, k)]
            t = 0
            while q:
                current_w, current = heapq.heappop(q)
                if current in visit:
                    continue
                visit.add(current)
                t = max(t, current_w)
                for (neiw, nei) in graph.get(current, []):
                    heapq.heappush(q, (neiw + current_w, nei))
            return t

        shortest = bfs_shortest(k)
        print('graph: ', graph)
        for node in graph:
            if node not in visit:
                print('not visit node: ', node)
                return -1
        return shortest
