class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def lcs(i, j) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0
            a = 0
            if text1[i] == text2[j]:
                # take i, j
                a = 1 + lcs(i + 1, j + 1)
            # skip i, j
            b = lcs(i + 1, j + 1)
            c = lcs(i, j + 1)
            d = lcs(i + 1, j)
            memo[(i, j)] = max(a, b, c, d)
            return memo[(i, j)]
        return lcs(0, 0)
