class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        memo = {}
        def can_sum_to_target(i, target: int) -> bool:
            if (i, target) in memo:
                return memo[(i, target)]
            if i >= len(nums):
                return False
            if target == 0:
                return True
            # take
            if nums[i] <= target:
                if can_sum_to_target(i + 1, target - nums[i]):
                    memo[(i, target)] = True
                    return True
            # don't take
            if can_sum_to_target(i + 1, target):
                memo[(i, target)] = True
                return True
            memo[(i, target)] = False
            return False

        tsum = sum(nums)
        if tsum % 2 != 0:
            return False
        return can_sum_to_target(0, tsum // 2)
