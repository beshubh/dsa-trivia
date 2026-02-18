class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        cur = []
        def dfs(i, current_sum):
            if i >= len(nums):
                if current_sum == target:
                    res.append(cur.copy())
                return
            if current_sum + nums[i] <= target:
                if current_sum + nums[i] == target:
                    res.append(cur + [nums[i]])
                else:
                    cur.append(nums[i])
                    dfs(i, current_sum + nums[i])
                    cur.pop()
            dfs(i + 1, current_sum)
        dfs(0, 0)
        return res
