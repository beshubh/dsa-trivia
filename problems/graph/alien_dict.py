from collections import deque, defaultdict


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # first letter where they differ is smaller in w1
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # longer is before shorter, so invalid ordering
                return ""

        q = deque([u for u in graph if indegree[u] == 0])
        order = []
        while q:
            u = q.pop()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.appendleft(v)
        return ''.join(order) if len(order) == len(graph.keys()) else ""
