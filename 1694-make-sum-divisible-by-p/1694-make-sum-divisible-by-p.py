class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        remainders = {0:-1}
        shortest = len(nums)

        cur = 0
        for i, num in enumerate(nums):
            cur += num
            mod = cur % p

            compl = (mod - rem) % p
            if compl in remainders:
                shortest = min(shortest, i - remainders[compl])

            remainders[mod] = i
        
        return shortest if shortest < len(nums) else -1