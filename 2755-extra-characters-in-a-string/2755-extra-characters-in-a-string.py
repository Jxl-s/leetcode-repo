class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}
        dictionary = set(dictionary)

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(s):
                return 0

            extra = 1 + dp(i + 1)
            for j in range(i+1, len(s)+1):
                if s[i:j] in dictionary:
                    extra = min(extra, dp(j))

            memo[i] = extra
            return memo[i]

        return dp(0)