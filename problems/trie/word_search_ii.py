
class TrieNode:

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False
        self.word: str | None = None

class PrefixTree:

    def __init__(self, root: TrieNode | None = None):
        self._root: TrieNode = root or TrieNode()


    def insert(self, word: str) -> None:
        current = self._root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.is_end = True
        current.word = word

    def search(self, word: str) -> bool:
        current = self._root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self._root
        for w in prefix:
            if w not in current.children:
                return False
            current = current.children[w]
        return True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = []
        visited = set()
        def dfs(row: int, col: int, current: TrieNode):

            if row >= len(board) or col >= len(board[row]) or row < 0 or col < 0:
                if current.is_end:
                    if current.word not in result:
                        result.append(current.word)
                return
            if current.is_end:
                if current.word not in result:
                    result.append(current.word)

            char = board[row][col]
            if char not in current.children:
                return

            if (row, col) not in visited:
                visited.add((row, col))
                dfs(row + 1, col, current.children[char])
                dfs(row, col + 1, current.children[char])
                dfs(row - 1, col, current.children[char])
                dfs(row, col - 1, current.children[char])
                visited.remove((row, col))

        root = TrieNode()
        index = PrefixTree(root)
        for word in words:
            index.insert(word)

        for row in range(len(board)):
            for col in range(len(board[row])):
                dfs(row, col, root)
        return result
