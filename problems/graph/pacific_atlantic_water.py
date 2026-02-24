import collections

NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []
        if not heights[0]:
            return []
        pacific_set = set()
        atlantic_set = set()
        def bfs(row: int, col: int, from_pacific: bool = True):
            ROWS, COLS = len(heights), len(heights[row])
            q = collections.deque([[row, col]])

            while q:
                row, col = q.pop()
                if from_pacific:
                    pacific_set.add((row, col))
                else:
                    atlantic_set.add((row, col))
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                        continue
                    if from_pacific and (r, c) in pacific_set:
                        continue
                    if not from_pacific and (r, c) in atlantic_set:
                        continue
                    if heights[r][c] >= heights[row][col]:
                        q.appendleft([r, c])

        result = []
        for c in range(len(heights[0])):
            bfs(0, c)

        for r in range(len(heights)):
            bfs(r, 0)

        # move inwards from atlantic
        for c in range(len(heights[0])):
            bfs(len(heights) - 1, c, False)

        for r  in range(len(heights)):
            bfs(r, len(heights[0]) - 1, False)

        result = list(pacific_set & atlantic_set)

        return result
