class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c in root:
                root = root[c]
            else:
                root[c] = {}
                root = root[c]

        root['.'] = True

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c in root:
                root = root[c]
            else:
                return False
        
        if '.' in root:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c in root:
                root = root[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)