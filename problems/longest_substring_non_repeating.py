
class Solution:

    def longestSubstringNonRepeating(self, s: str) -> int:
        """
        we keep moving to the right, and if we find a char that is repeating we can then
        move our left pointer to the right, and keep moving.
        """
        left, char_set = 0, set()
        res = 0
        for right in range(len(s)):
            if s[right] in char_set:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1

            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubstringNonRepeating('abcabcbb'))
