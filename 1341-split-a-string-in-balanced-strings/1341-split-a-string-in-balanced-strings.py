class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0

        r_count = 0
        l_count = 0
        
        for c in s:
            if c == 'R':
                r_count += 1
            if c == 'L':
                l_count += 1
                
            if r_count == l_count and r_count > 0:
                r_count = 0
                l_count = 0
                count += 1

        return count