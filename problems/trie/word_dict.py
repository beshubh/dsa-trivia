
class TrieNode:

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self._root: TrieNode = TrieNode()


    def addWord(self, word: str) -> None:
        current = self._root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.is_end = True

    def search(self, word: str) -> bool:


        def dfs(idx: int = 0, root: TrieNode = self._root):
            if idx >= len(word):
                return root.is_end
            if word[idx] in root.children:
                return dfs(idx + 1, root.children[word[idx]])
            elif word[idx] == '.':
                for child in root.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                return False
        return dfs(0, self._root)
