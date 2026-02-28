import collections

class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        outdegree = collections.defaultdict(int)
        nodes = set()
        for u, v in pairs:
            graph[u].append(v)
            indegree[v] += 1
            outdegree[u] += 1
            nodes.add(u)
            nodes.add(v)

        route = []
        def dfs(node: int) -> None:
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            route.append(node)
        start = pairs[0][0]
        for node in nodes:
            if outdegree[node] - indegree[node] == 1: # its the start node
                start = node
                break
        dfs(start)
        route = route[::-1]
        output = []
        for i in range(len(route) - 1):
            output.append([route[i], route[i + 1]])
        return output
