import unittest
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        def dfs(row, col):
            if  row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            if board[row][col] == 'X':
                return
            if board[row][col] == 'T':
                return
            board[row][col] = 'T'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or c == 0 or r == len(board) - 1 or c == len(board[r]) - 1:
                    dfs(r, c)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'T':
                    board[r][c] = 'O'





class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = Solution()

    def test_solve(self):
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        self.runner.solve(board)
        self.assertEqual(board, [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ])
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        self.runner.solve(board)
        self.assertEqual(board, [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ])
