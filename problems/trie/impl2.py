

class TrieNode:

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self._root: TrieNode = TrieNode()


    def insert(self, word: str) -> None:
        current = self._root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.is_end = True

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
