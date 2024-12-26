class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        rows = { x: i for i in range(len(rows)) for x in rows[i] }
        
        output = []
        for word in words:
            lower = word.lower()
            row = rows[lower[0]]
            if all(rows[c] == row for c in lower):
                output.append(word)

        return output