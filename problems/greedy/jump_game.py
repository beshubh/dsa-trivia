class Solution:
    def canJump(self, nums: list[int]) -> bool:
        def can_jump(i: int) -> bool:
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for j in range(1, nums[i] + 1):
                if can_jump(i + j):
                    return True
            return False

        return can_jump(0)


class SolutionGreedy:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if goal - i <= nums[i]:
                goal = i
        return goal == 0
