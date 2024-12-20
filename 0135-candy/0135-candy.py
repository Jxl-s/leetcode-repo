class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies_left = [0] * n
        candies_left[0] = 1

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies_left[i] = candies_left[i - 1] + 1
            else:
                candies_left[i] = 1

        candies_right = [0] * n
        candies_right[n-1] = 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_right[i] = candies_right[i + 1] + 1
            else:
                candies_right[i] = 1
        
        candies = [0] * n
        for i in range(n):
            candies[i] = candies_left[i] + candies_right[i]
        
        # Normalize candy, so that lowest is 1
        low = min(candies) - 1
        for i in range(n):
            candies[i] -= low

        # Normalize neighbors, so max diff between neighbors is 1
        for i in range(1, n - 1):
            diff = min(candies[i] - candies[i - 1], candies[i] - candies[i + 1]) - 1
            if diff > 0:
                candies[i] -= diff
        
        return sum(candies)