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


def lis_table(nums: list[int]) -> int:
    table = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
    n = len(nums)
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -2, -1):
            # skip
            skip = table[i + 1][j + 1]
            # take
            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + table[i + 1][i + 1]
            table[i][j + 1] = max(skip, take)
    return table[0][0]
