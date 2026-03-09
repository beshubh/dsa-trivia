class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def uniqpaths(m, n) -> int:
            if (m, n) in memo:
                return memo[(m, n)]
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            # down
            memo[(m, n)] = uniqpaths(m - 1, n) + uniqpaths(m, n - 1)
            return memo[(m, n)]
        return uniqpaths(m,n)
