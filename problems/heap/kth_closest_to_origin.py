import math
import heapq


class Solution:
    def euclidean_dist(self, p1, p2) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        p0 = (0, 0)
        distances = []
        for pi in points:
            dist = self.euclidean_dist(p0, pi)
            distances.append((dist, pi))
        heapq.heapify(distances)
        res = []
        while k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1
        return res
