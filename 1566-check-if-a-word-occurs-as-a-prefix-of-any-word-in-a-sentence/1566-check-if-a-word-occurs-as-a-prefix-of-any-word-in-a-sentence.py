class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:        
        trie = {}
        for i, word in enumerate(sentence.split(' ')):
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}

                root = root[c]
                if '.' not in root:
                    root['.'] = i + 1

        root = trie
        for c in searchWord:
            if c not in root:
                return -1
            
            root = root[c]
        
        return root['.']