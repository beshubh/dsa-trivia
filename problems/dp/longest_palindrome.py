class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 1:
        #     return s
        result = ''
        for i in range(len(s)): # N
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l > len(result):
                result = s[l + 1: r]
            # even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l > len(result):
                result = s[l + 1: r]
        return result
