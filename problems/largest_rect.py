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

class SolutionOptimized:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        res = 0
        # n = 2
        # [0, 1, 2, 3, 4, 5] # index
        # [7, 1, 7, 2, 2, 4] # input

        # [0, 0, 2, 2, 2, 5] # left indices

        # [0, 5, 2, 5, 5, 5] # right indices

        # [7, 5, 7, 8, 8, 5] # output will be max of this

        # [1, 1]
        # [0, 0] left
        # [1, 1] right
        # [2, 2]
        left_pass = [None] * len(heights)
        stack = []
        for i in range(len(heights)):
            cur_height = heights[i]
            while stack and heights[stack[-1]] >= cur_height:
                stack.pop()
            if stack:
                left_pass[i] = stack[-1] + 1
            else:
                left_pass[i] = 0
            stack.append(i)

        print('left pass', left_pass)
        stack = []
        right_pass = [None] * len(heights)
        for i in reversed(range(len(heights))):
            cur_height = heights[i]
            while stack and heights[stack[-1]] >= cur_height:
                stack.pop()
            if stack:
                right_pass[i] = stack[-1] - 1
            else:
                right_pass[i] = len(heights) - 1
            stack.append(i)
        print('right pass', right_pass)

        for i, (right, left) in enumerate(zip(right_pass, left_pass)):
            width = right - left  + 1
            height = heights[i]
            res = max(width * height, res)
        return res
