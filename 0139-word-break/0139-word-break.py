class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(s2):
            if s2 in memo:
                return memo[s2]

            if len(s2) == 0:
                return True

            for w in wordDict:
                if s2.startswith(w):
                    if dp(s2[len(w):]):
                        memo[s2] = True
                        return True

            memo[s2] = False
            return False
        
        return dp(s)