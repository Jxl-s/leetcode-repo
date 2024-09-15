class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s):
            is_found = False
            while j < len(t):
                if s[i] == t[j]:
                    is_found = True
                    j += 1
                    break
                
                j += 1
            
            if not is_found:
                return False

            i += 1
        
        return True