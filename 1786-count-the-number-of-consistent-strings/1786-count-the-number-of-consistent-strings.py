class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            is_good = True
            for c in word:
                if c not in allowed:
                    is_good = False
                    break
            
            if is_good:
                count += 1
        
        return count