class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}
        def f(i, amount_needed: int):
            if i >= len(coins):
                return float('inf')
            if amount_needed == 0:
                return 0
            if amount_needed < 0:
                return float('inf')
            if (i, amount_needed) in memo:
                return memo[(i, amount_needed)]
            res = min(1 + f(i, amount_needed - coins[i]), f(i + 1, amount_needed))
            memo[(i, amount_needed)] = res
            return res
        ans = f(0, amount)
        if ans == float('inf'):
            return -1
        return ans
