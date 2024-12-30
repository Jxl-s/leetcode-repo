MOD = 10**9 + 7

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(length):
            if length > high:
                return 0

            answer = 0
            if length >= low:
                answer = 1

            answer += dp(length + zero) + dp(length + one)
            answer %= MOD
            return answer

        return dp(0)