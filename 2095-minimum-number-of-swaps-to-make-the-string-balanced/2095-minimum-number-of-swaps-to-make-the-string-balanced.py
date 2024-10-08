class Solution:
    def minSwaps(self, s: str) -> int:
        closed = 0
        max_closed = 0

        for c in s:
            if c == ']': closed += 1
            if c == '[': closed -= 1
            max_closed = max(max_closed, closed)

        return (max_closed + 1) // 2