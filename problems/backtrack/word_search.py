class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        def backtrack(row, col, word_idx = 0):
            if word_idx >= len(word):
                return True
            if row >= len(board) or col >= len(board[row]) or row < 0 or col < 0:
                return False
            if (row, col) not in visited and board[row][col] == word[word_idx]:
                visited.add((row, col))
                res = (
                    backtrack(row - 1, col, word_idx + 1) or
                    backtrack(row + 1, col, word_idx + 1) or
                    backtrack(row, col + 1, word_idx + 1) or
                    backtrack(row, col - 1, word_idx + 1)
                )
                visited.remove((row, col))
                return res

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0] and backtrack(r, c):
                    return True
        return False
