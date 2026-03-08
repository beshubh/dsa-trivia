class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        memo = [-1] * (N + 1)
        nums1 = [nums[i] for i in range(N - 1)]
        nums2 = [nums[i] for i in range(1, N)]

        def f(i, nums, memo):
            if i < 0:
                return 0
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + f(i + 2, nums, memo), f(i + 1, nums, memo))
            return memo[i]
        return max(f(0, nums1, memo.copy()), f(0, nums2, memo.copy()))
