import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        print('max_heap: ', max_heap)
        while max_heap:
            if len(max_heap) <= 1:
                return -max_heap[0]
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            print('x: ', x, ' y: ', y)
            if x == y:
                continue
            else:
                y = y - x
                heapq.heappush(max_heap, -y)
        return 0
