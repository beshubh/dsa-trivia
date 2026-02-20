class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        def dfs(idx: int = 0, cur = []):
            if idx == len(nums):
                result.append(cur)
                return

            # include this element
            dfs(idx + 1, cur + [nums[idx]])
            # skip all the similar elements
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            # exclude this element
            dfs(idx + 1, cur)

        dfs()
        return result
