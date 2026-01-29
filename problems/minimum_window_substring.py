

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window_count = [0] * (26 + 26 + 6), [0] * (26 + 26 + 6)
        for i in range(len(t)):
            t_count[ord(t[i]) - ord("A")] += 1

        left, res = 0, ""
        required, formed = len(list(set(t))), 0
        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            window_count[index] += 1
            if window_count[index] == t_count[index]:
                formed += 1
            while formed == required:
                window_len = right - left + 1
                if len(res) == 0 or window_len < len(res):
                    res = s[left: right + 1]
                index = ord(s[left]) - ord('A')
                window_count[index] -= 1
                if window_count[index] < t_count[index]:
                    formed -= 1
                left += 1
        return res


if __name__ == "__main__":
    solution = Solution().minWindow("ADOBECODEBANC", "ABC")
    print(solution)
