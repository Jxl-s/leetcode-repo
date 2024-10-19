class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
                if i >= len(s):
                    return True
        
        return False