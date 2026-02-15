import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.max_heap = []
        for n in nums:
            heapq.heappush(self.max_heap, n)
            while len(self.max_heap) >= k:
                heapq.heappop(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val)
        while len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)
        return self.max_heap[0]
