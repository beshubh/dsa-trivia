
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {x: [] for x in range(numCourses)}
        for (c1, c2) in prerequisites:
            graph[c1].append(c2)

        # 0 for not visisted, 1 for visiting currently, 2 for visited
        state = {node: 0 for node in graph}
        for u in graph:
            for v in graph:
                if v not in state:
                    state[v] = 0
        order = []
        def dfs_cycle(start) -> bool:
            state[start] = 1 # mark current visiting
            for nei in graph.get(start, []):
                if state[nei] == 1: # there is a back edge so cycle
                    return True
                if state[nei] == 0 and dfs_cycle(nei):
                    return True
            state[start] = 2
            return False
        possible = True
        for node in graph:
            if state[node] == 0:
                if dfs_cycle(node):
                    possible = False
                    break
        return order if possible else []
