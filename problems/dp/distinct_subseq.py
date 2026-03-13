class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo: dict[tuple[int, int], int] = {}

        def num_ds(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            c1 = 0
            if s[i] == t[j]:
                c1 = num_ds(i + 1, j + 1)
            c2 = num_ds(i + 1, j)
            memo[(i, j)] = c1 + c2
            return memo[(i, j)]

        return num_ds(0, 0)
