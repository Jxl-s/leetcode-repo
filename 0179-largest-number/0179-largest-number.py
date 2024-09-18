class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(sorted(list(map(str, nums)), key=lambda x: x*10, reverse=True))
        return largest if largest[0] != '0' else '0'