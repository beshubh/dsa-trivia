import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for num in nums:  # n
            heapq.heappush(min_heap, num)  # log k
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        # nlogk
        return min_heap[0]
