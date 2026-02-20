class Solution:

    def can_place(self, board: list[list[str]], row: int, col: int) -> bool:
        if board[row][col] == 'Q':
            return False

        # left diagonal
        c = col
        for r in range(row, -1, -1):
            if c >= 0 and board[r][c] == 'Q':
                return False
            c -= 1

        # right diagonal
        r = row
        for c in range(col, len(board), 1):
            if r >= 0 and board[r][c] == 'Q':
                return False
            r -= 1

        # left bottom diagonal
        r = row
        for c in range(col, -1, -1):
            if r < len(board) and board[r][c] == 'Q':
                return False
            r += 1

        # right bottom diaglonal
        c = col
        for r in range(row, len(board), 1):
            if c < len(board) and board[r][c] == 'Q':
                return False
            c += 1

        # same row
        for c in range(len(board)):
            if board[row][c] == 'Q':
                return False
        # same column
        for r in range(len(board)):
            if board[r][col] == 'Q':
                return False
        return True

    def format_board(self, board):
        return [''.join(b) for b in board]


    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        def place(board, row):
            if n == row:
                result.append(self.format_board(board))
                return
            if row >= len(board):
                return
            for col in range(n):
                if self.can_place(board, row, col):
                    board[row][col] = 'Q'
                    place(board, row + 1)
                    board[row][col] = '.'

        place(board, 0)
        return result
