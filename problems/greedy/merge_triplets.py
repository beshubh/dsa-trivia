class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        t0_exists = t1_exists = t2_exists = False
        for t0, t1, t2 in triplets:
            if target[0] < t0 or target[1] < t1 or target[2] < t2:
                continue
            if t0 == target[0]:
                t0_exists = True
            if t1 == target[1]:
                t1_exists = True
            if t2 == target[2]:
                t2_exists = True
        return t1_exists and t2_exists and t0_exists
