
class PrefixTree:

    def __init__(self):
        self._root = {}


    def insert(self, word: str) -> None:
        current = self._root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['is_end'] = True

    def search(self, word: str) -> bool:
        current = self._root
        for w in word:
            if w not in current:
                return False
            current = current[w]
        return current.get('is_end', False) or False

    def startsWith(self, prefix: str) -> bool:
        current = self._root
        for w in prefix:
            if w not in current:
                return False
            current = current[w]
        return True
