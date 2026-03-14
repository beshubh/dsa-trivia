class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, tank = 0, 0
        for i, g in enumerate(gas):
            tank += g - cost[i]
            if tank < 0:
                # current start is dead it cannot complete the curcuit.
                start = i + 1
                tank = 0
        return start
