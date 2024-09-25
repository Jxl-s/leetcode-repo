class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for w in words:
            root = trie
            for c in w:
                if c not in root:
                    root[c] = {'-': 0}

                root = root[c]
                root['-'] += 1
        
        output = []
        for w in words:
            root = trie
            score = 0

            for c in w:
                root = root[c]
                score += root['-']
            
            output.append(score)
        
        return output