class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        use_one = True
        output = ""

        while i < len(word1) or j < len(word2):
            target = 1 if use_one else 2
            if i >= len(word1): target = 2
            if j >= len(word2): target = 1

            use_one = not use_one

            if target == 1:
                output += word1[i]
                i += 1
            else:
                output += word2[j]
                j += 1
        
        return output
