class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best_sum = float('-inf')
        running_sum = 0
        for i, n in enumerate(nums):
            if running_sum + n > n:
                running_sum += n
            else:
                running_sum = n
            best_sum = max(best_sum, running_sum)
        return best_sum  # type: ignore
