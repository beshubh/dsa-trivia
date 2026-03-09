class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        memo = {}
        def lis(i: int = 0, j: int = -1) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(nums):
                return 0
            # take
            a = -1
            if j == -1 or nums[i] > nums[j]:
                a = 1 + lis(i + 1, i)
            # skip
            b = lis(i + 1, j)
            memo[(i, j)] = max(a, b)
            return memo[(i, j)]
        return lis()
