class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        s2 = s[::-1]
        n = len(s)

        for i in range(n):
            if s.startswith(s2[i:]):
                return s2[:i] + s

        return s2 + s