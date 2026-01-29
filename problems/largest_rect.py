class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        res = 0
        # n = 2
        for i, h in enumerate(heights):
            left, right = i, i
            while left > 0 and heights[left - 1] >= h:
                left -= 1

            while right  + 1 < len(heights) and heights[right + 1] >= h:
                right += 1
            width = right - left  + 1
            height = h
            res = max(width * height, res)
        return res
