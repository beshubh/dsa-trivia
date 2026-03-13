class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        result = 0
        memo = {}
        indegrees = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                indegrees[(r, c)] = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                for dr, dc in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if (
                        nr >= 0
                        and nc >= 0
                        and nr < len(matrix)
                        and nc < len(matrix[r])
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        indegrees[(nr, nc)] += 1
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if indegrees[(r, c)] == 0:
                    result = max(lip(matrix, r, c, memo), result)
        return result


NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def lip(matrix: list[list[int]], r: int, c: int, memo: dict) -> int:
    if (r, c) in memo:
        return memo[(r, c)]
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
        return 0
    choices = []
    for dr, dc in NEIGHBORS:
        nr, nc = r + dr, c + dc
        if nr >= 0 and nc >= 0 and nr < len(matrix) and nc < len(matrix[r]) and matrix[nr][nc] > matrix[r][c]:
            choices.append(lip(matrix, nr, nc, memo))
    memo[(r, c)] = 1 + max(choices or [0])
    return memo[(r, c)]
