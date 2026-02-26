class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = {x: [] for x in range(n)}
        for (src, dst) in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph.get(node, []):
                if nei not in visited:
                    dfs(nei)
        visit_iter = set()
        def dfs_iter(node):
            stack = [node]
            visit_iter.add(node)
            while stack:
                print('visit iter', visit_iter)
                current = stack.pop()
                for nei in reversed(graph.get(current, [])):
                    if nei not in visit_iter:
                        visit_iter.add(nei)
                        stack.append(nei)


        connected_components = 0
        for node in graph:
            if node not in visit_iter:
                dfs_iter(node)
                connected_components += 1
        return connected_components
