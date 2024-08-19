class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = {}
        return self.helper(amount, coins, 0)

    def helper(self, amount, coins, start):
        if amount == 0:
            return 1

        if (amount, start) in self.memo:
            return self.memo[(amount, start)]

        count = 0
        for i in range(start, len(coins)):
            remainder = amount - coins[i]
            if remainder >= 0:
                count += self.helper(remainder, coins, i)
        
        self.memo[(amount, start)] = count
        return self.memo[(amount, start)]