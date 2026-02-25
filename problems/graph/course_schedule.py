import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        if len(prerequisites) == 0:
            return True
        graph = collections.defaultdict(list)
        for (c1, c2) in prerequisites:
            graph[c2].append(c1)

        # 0 univisted, 1 visiting, 2 visited
        state = {node: 0 for node in graph}
        # ensure state exsists for all the neighbors
        for u in graph:
            for v in graph[u]:
                if v not in state:
                    state[v] = 0

        def dfs(node: int) -> bool:
            state[node] = 1 # mark visiting

            for nei in graph.get(node, []):
                if state[nei] == 1:
                    return True # visiting the node in same route

                if state[nei] == 0 and dfs(nei): # cycle at the neighbor
                    return True
            state[node] = 2
            return False

        can_complete = True
        for node in state:
            if state[node] == 0:
                if dfs(node):
                    can_complete = False
                    break
        return can_complete
