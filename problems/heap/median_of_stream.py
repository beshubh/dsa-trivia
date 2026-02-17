import heapq


class MedianStream:
    def __init__(self):
        self._lowerhalf = []  # all elements less or equal to median, with maximum at the top, max heap
        self._upperhalf = []  # all elements greater or equal to median, with minimum at the top, min heap

    def addNum(self, num: int) -> None:
        self._size += 1
        heapq.heappush(self._lowerhalf, -num)
        heapq.heappush(self._upperhalf, -heapq.heappop(self._lowerhalf))

        if len(self._upperhalf) > len(self._lowerhalf):
            heapq.heappush(self._lowerhalf, -heapq.heappop(self._upperhalf))

    def findMedian(self) -> float:
        if (len(self._upperhalf) + len(self._lowerhalf)) % 2 == 0:
            return (-self._lowerhalf[0] + self._upperhalf[0]) / 2
        else:
            return self._lowerhalf[0]
