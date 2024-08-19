class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        return self.helper(coins, amount)
    
    def helper(self, coins, amount):
        if amount == 0:
            return 0

        if amount in self.memo:
            return self.memo[amount]

        min_times = float("inf")
        for i in range(len(coins)):
            if amount - coins[i] < 0:
                continue

            result = self.helper(coins, amount - coins[i])
            if result != -1:
                min_times = min(min_times, result + 1)

        self.memo[amount] = -1 if min_times == float("inf") else min_times
        return self.memo[amount]