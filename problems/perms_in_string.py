
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        if s1 is perm of s2.
        the substring of s2 must be the same length as s1.
        frequency of each character must match exactly.
        so the window size will be fixed to the lenght of s1.

        to do this we need to compare the char counts of s1 against char counts of s2 of the current window.
        """
        s1_count, window_count = [0] * 26, [0] * 26
        if len(s1) > len(s2):
            return False

        for i, c in enumerate(s1):
            s1_count[ord(c) - ord('a')] = 1 + s1_count[ord(c)]
            window_count[ord(s2[i]) - ord('a')] = 1 + window_count[ord(s2[i])]

        left = 0
        if s1_count == window_count:
            return True

        for right in range(len(s1), len(s2)):
            leaving_char = ord(s2[left]) - ord('a')
            new_char = ord(s2[right]) - ord('a')

            window_count[leaving_char] -= 1
            window_count[new_char] += 1
            left += 1
            if s1_count == window_count:
                return True

        return False


if __name__ == '__main__':
    solution = Solution().checkInclusion('ab', 'aab')
    print(solution)
