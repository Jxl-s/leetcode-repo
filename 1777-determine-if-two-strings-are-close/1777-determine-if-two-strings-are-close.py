class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        ord_a = ord('a')

        for c in word1:
            c1[ord(c) - ord_a] += 1

        for c in word2:
            c2[ord(c) - ord_a] += 1
        
        for i in range(26):
            if c1[i] > 0 and c2[i] == 0:
                return False

            if c2[i] > 0 and c1[i] == 0:
                return False

        c1.sort()
        c2.sort()

        for i in range(26):
            if c1[i] != c2[i]:
                return False
        
        return True