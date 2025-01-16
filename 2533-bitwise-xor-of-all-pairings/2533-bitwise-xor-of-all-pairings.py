class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums1) % 2 == 1:
            for x in nums2:
                result ^= x

        if len(nums2) % 2 == 1:
            for x in nums1:
                result ^= x

        return result