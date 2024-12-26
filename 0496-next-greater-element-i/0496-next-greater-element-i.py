class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        indexes = {x: i for i, x in enumerate(nums2)}

        elements = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums2[stack[-1]] <= nums2[i]:
                elements[stack.pop()] = nums2[i]
            
            stack.append(i)

        return [elements[indexes[x]] for x in nums1]