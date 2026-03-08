class Solution:

    def countSubstrings(self, s: str) -> int:
        result = 0 # 5

        for i in range(len(s)): # i = 2
            # check for palindromes
            # odd length
            l, r = i, i # 2, 2
            while l >= 0 and r < len(s) and s[l] == s[r]: # 0, 2
                l -= 1 # -1
                r += 1 # 3
                result += 1

            # even length
            l, r = i, i + 1 # 2, 3
            while l >= 0 and r < len(s) and s[l] == s[r]: # 1, 2
                l -= 1 # 0
                r += 1 # 3
                result += 1
        return result
