class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = 0

        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                if stack > 0:
                    stack -= 1
                else:
                    count += 1
        
        return count + stack