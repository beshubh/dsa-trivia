class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def perms(depth: int = 0, available = [True for _ in nums], cur_result = [0 for _ in nums]):
            if all([not av for av in available]):
                result.append(cur_result.copy())
            for i, av in enumerate(available):
                if av:
                    cur_result[depth] = nums[i]
                    available[i] = False
                    perms(depth + 1, available, cur_result)
                    available[i] = True

        perms()
        return result
