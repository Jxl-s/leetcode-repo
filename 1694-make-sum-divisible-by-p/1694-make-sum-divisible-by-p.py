class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        remainders = { 0: -1 }
        prefix = 0
        shortest = len(nums)

        for i, num in enumerate(nums):
            prefix += num
            mod = prefix % p
            complement = (mod - rem) % p

            if complement in remainders:
                shortest = min(shortest, i - remainders[complement])
            
            remainders[mod] = i

        return shortest if shortest != len(nums) else -1