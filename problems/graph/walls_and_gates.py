import collections

INF = 2147483647
NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return None
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(row: int, col: int):
            q = collections.deque([(row, col)])
            visited  = set()
            while q:
                (row, col) = q.pop()
                visited.add((row, col))
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if not (r in range(ROWS) and c in range(COLS) and (r, c) not in visited):
                        continue
                    if grid[r][c] in [0, -1]:
                        continue
                    grid[r][c] = min(grid[row][col] + 1, grid[r][c])
                    q.appendleft((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    bfs(row, col)
a
