

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(open: int = 0, close: int = 0, current = []):
            if close > open or open > n:
                return

            if open == close  and close == n:
                result.append(''.join(current))
                return

            backtrack(open + 1, close, current + ['('])
            if open > close:
                backtrack(open, close + 1, current + [')'])
        backtrack()
        return result
