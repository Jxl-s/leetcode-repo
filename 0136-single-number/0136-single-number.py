class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            mask ^= n
        
        return mask