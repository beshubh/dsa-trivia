from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True) # so we get the smallest at the end in O(1)

        route = []  # we will build the route in reverse order
        def dfs(src: str) -> None:
            while graph[src]:
                nxt = graph[src].pop()
                dfs(nxt)

            # there is no outgoing edge that remains, add to the routes
            route.append(src)
        dfs("JFK")
        return route[::-1]
