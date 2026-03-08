class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [-1] * (len(nums) + 1)
        def f(i):
            if i < 0:
                return 0
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + f(i + 2), f(i + 1))
            return memo[i]
        return f(0)
