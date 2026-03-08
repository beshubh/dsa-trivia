class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = [-1] * (len(cost) + 1)

        def f(i=0):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(f(i + 1), f(i + 2))
            return memo[i]
        return min(f(0), f(1))
