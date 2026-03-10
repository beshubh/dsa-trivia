class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        def f(i: int, total_sum: int = 0) -> int:
            if (i, total_sum) in memo:
                return memo[(i, total_sum)]
            if i >= len(nums):
                if target == total_sum:
                    return 1
                return 0
            # add, sub
            memo[(i, total_sum)] = f(i + 1, total_sum + nums[i]) + f(i + 1, total_sum - nums[i])
            return memo[(i, total_sum)]
        return f(0, 0)
