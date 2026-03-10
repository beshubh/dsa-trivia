class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}
        def max_profit(i: int, buying: bool = True):
            if (i, buying) in memo:
                return memo[(i, buying)]
            # gives me the maximum profit if I buy or sell at i
            if i >= len(prices):
                return 0
            if buying:
                buy =  max_profit(i + 1, False) - prices[i]
                skip = max_profit(i + 1, buying)
                memo[(i, buying)] = max(buy, skip)
                return memo[(i, buying)]
            else:
                sell = prices[i] + max_profit(i + 2, True)
                hold = max_profit(i + 1, buying)
                memo[(i, buying)] = max(sell, hold)
                return memo[(i, buying)]
        return max_profit(0)
