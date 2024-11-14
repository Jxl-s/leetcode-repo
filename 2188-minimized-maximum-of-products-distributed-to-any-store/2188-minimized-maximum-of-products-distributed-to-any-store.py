class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(amount):
            stores = 0

            # ceil(q / amount) represents how many stores are required for each product
            for q in quantities:
                stores += ceil(q / amount)

            # if required is less than n, we can distribute
            return stores <= n

        left = 1
        right = max(quantities)

        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left