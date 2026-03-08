class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def f(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            # take i
            res = f(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                res += f(i + 2)
            memo[i] = res
            return res
        return f(0)
