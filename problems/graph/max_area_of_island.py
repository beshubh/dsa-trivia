import collections

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row: int, col: int):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            area = 1
            while q:
                row, col = q.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                        visited.add((r, c))
                        q.appendleft((r, c))
                        area += 1
            print('aread: ', area)
            return area

        islands = 0
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(bfs(row, col), max_area)
                    islands += 1
        return max_area
