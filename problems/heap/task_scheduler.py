from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-c for c in counter.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while q or max_heap:
            time += 1
            if max_heap:
                rem_count = 1 + heapq.heappop(max_heap)
                if rem_count:
                    q.appendleft((rem_count, time + n))
            if q and q[-1][1] == time:
                # reason we are not decreasing count from queue and then pushing to the heap is because q already contains the remaining count only
                heapq.heappush(max_heap, q.pop()[0])
        return time
