class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count('1')
        left = 0
        score = 0

        for i in range(len(s)-1):
            if s[i] == '0': left += 1
            if s[i] == '1': right -= 1

            score = max(score, left + right)

        return score