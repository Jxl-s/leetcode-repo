class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maximums = defaultdict(int)
        items.sort()

        max_so_far = 0
        for price, beauty in items:
            max_so_far = max(max_so_far, beauty)
            maximums[price] = max_so_far

        prices = sorted(maximums.keys())

        n = len(queries)
        answer = [0] * n

        for i in range(n):
            index = bisect_right(prices, queries[i])
            if index > 0:
                answer[i] = maximums[prices[index - 1]]

        return answer