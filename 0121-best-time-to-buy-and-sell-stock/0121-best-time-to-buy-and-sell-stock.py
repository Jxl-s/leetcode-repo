class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought_at = prices[0]
        max_profit = 0

        for p in prices:
            if p > bought_at:
                max_profit = max(max_profit, p - bought_at)
            
            if p < bought_at:
                bought_at = p

        return max_profit