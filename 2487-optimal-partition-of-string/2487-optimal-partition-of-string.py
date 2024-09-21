class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        chars = set()

        for c in s:
            if c in chars:
                count += 1
                chars.clear()

            chars.add(c)
        
        return count + 1