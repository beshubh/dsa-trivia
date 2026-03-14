class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def edit_distance(i: int, j: int) -> int:
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return len(word2) - j
            if word1[i] == word2[j]:
                return edit_distance(i + 1, j + 1)
            # insert
            a = 1 + edit_distance(i, j + 1)
            # delete
            b = 1 + edit_distance(i + 1, j)
            # replace
            c = 1 + edit_distance(i + 1, j + 1)
            return min(a, b, c)

        return edit_distance(0, 0)
