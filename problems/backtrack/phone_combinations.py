

CHARS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        def backtrack(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return [c for c in CHARS[digits]]
            current = []
            for c in CHARS[digits[0]]:
                combination_suffixes = backtrack(digits[1:])
                for cs in combination_suffixes:
                    current.append(c + cs)
            return current
        result = backtrack(digits)
        return result
