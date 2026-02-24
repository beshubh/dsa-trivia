import collections


NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


class Solution:
    def check_if_impossible(self, grid: list[list[int]], visited: set) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    return True
        return False


    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if all(grid[row][col] == 1 for row in range(ROWS) for col in range(COLS)):
            return -1
        if all(grid[row][col] == 0 for row in range(ROWS) for col in range(COLS)):
            return 0
        if all(grid[row][col] == 1 or grid[row][col] == 0 for row in range(ROWS) for col in range(COLS)):
            return -1

        distance = [[0 if grid[row][col] in [2, 0] else float('inf') for col in range(COLS)] for row in range(ROWS)]

        def bfs(row: int, col: int) -> int:
            visited = set()
            q = collections.deque([(row, col)])
            max_distance = 0
            while q:
                row, col = q.pop()
                visited.add((row, col))
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc

                    if r not in range(ROWS) or c not in range (COLS):
                        continue

                    if (r, c) in visited or grid[r][c] in [2, 0]:
                        visited.add((r, c))
                        continue
                    distance[r][c]  = min(distance[r][c], distance[row][col] + 1)
                    max_distance = max(max_distance, distance[r][c])
                    q.appendleft((r, c))

            if self.check_if_impossible(grid, visited):
                return float('inf')
            return max_distance

        ans = float('inf')
        no_rotten = True
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    ans = min(ans, bfs(row, col))
                    no_rotten = False
        if no_rotten:
            return 0
        if ans == float('inf'):
            return -1
        return ans
