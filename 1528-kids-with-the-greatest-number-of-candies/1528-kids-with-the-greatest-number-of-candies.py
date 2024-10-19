class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [True if candies[i] + extraCandies >= max_candy else False for i in range(len(candies))]