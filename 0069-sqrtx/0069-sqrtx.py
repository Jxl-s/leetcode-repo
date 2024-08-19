class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 1
        high = x // 2
        
        while low <=high:
            mid = (low + high) // 2
            mult = mid * mid

            if mult == x:
                return mid
            elif mult < x:
                low = mid + 1
            else:
                high = mid - 1

        return high