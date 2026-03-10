class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}
        def f(i: int, amount: int) -> int:
            if (i, amount) in memo:
                return memo[(i, amount)]
            if i >= len(coins):
                return 0
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            # use this coin, skip this coin
            memo[(i, amount)] = f(i, amount - coins[i]) + f(i + 1, amount)
            return memo[(i, amount)]
        return f(0, amount)
