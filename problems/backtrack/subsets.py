class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def inner(idx = 0, cur = []):
            if idx == len(nums):
                res.append(cur)
                return
            inner(idx + 1, cur) # exclude
            inner(idx + 1, cur + [nums[idx]]) # include
        inner()
        return res
