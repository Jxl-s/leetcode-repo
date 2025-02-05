class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False

        return sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1))) <= 2