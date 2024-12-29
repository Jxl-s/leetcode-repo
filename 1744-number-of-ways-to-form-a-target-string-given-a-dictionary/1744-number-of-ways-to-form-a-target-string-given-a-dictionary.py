MOD = 10**9 + 7

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        counts = [[0] * 26 for _ in range(len(words[0]))]

        for word in words:
            for i, c in enumerate(word):
                counts[i][ord(c) - ord('a')] += 1

        # ith character of target, kth character of words
        @cache
        def dp(k, i):
            if i == len(target):
                return 1
            
            if k == len(words[0]):
                return 0

            count = dp(k + 1, i)
            possible = counts[k][ord(target[i]) - ord('a')]

            if possible > 0:
                count += possible * dp(k + 1, i + 1)
                count %= MOD

            return count

        return dp(0, 0)