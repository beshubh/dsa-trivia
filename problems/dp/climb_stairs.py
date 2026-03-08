class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def f(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if memo[n] != -1:
                return memo[n]
            memo[n] = f(n - 1) + f(n - 2)
            return memo[n]
        return f(n)
