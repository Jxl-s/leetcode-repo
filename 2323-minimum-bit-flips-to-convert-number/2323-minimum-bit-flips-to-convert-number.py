class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start)[2:]
        g = bin(goal)[2:]
        
        if len(s) < len(g):
            s = (len(g) - len(s)) * '0' + s
        elif len(s) > len(g):
            g = (len(s) - len(g)) * '0' + g

        flips = 0
        for i in range(len(s)):
            if s[i] != g[i]:
                flips += 1

        return flips