class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        mask = (1 << maximumBit) - 1

        current = nums[0]
        output = [0] * n
        output[0] = mask ^ nums[0]

        for i in range(1, n):
            current ^= nums[i]
            output[i] = mask ^ current

        return output[::-1]