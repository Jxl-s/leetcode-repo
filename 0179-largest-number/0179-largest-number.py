class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        strs.sort(key=lambda x: x*10, reverse=True)

        largest_num = ''.join(strs)
        return largest_num if largest_num[0] != '0' else '0'