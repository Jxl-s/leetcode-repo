class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        pattern_s = ''
        pattern_t = ''

        for c in s:
            if c not in seen_s:
                seen_s[c] = len(seen_s) + 1
            
            pattern_s += str(seen_s[c])
        
        for c in t:
            if c not in seen_t:
                seen_t[c] = len(seen_t) + 1
            
            pattern_t += str(seen_t[c])
        
        return pattern_s == pattern_t