nums = [
    ['M', 1000],
    ['CM', 900],
    ['D', 500],
    ['CD', 400],
    ['C', 100],
    ['XC', 90],
    ['L', 50],
    ['XL', 40],
    ['X', 10],
    ['IX', 9],
    ['V', 5],
    ['IV', 4],
    ['I', 1],
]

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        i = 0
        while num > 0 and i < len(nums):
            if nums[i][1] > num:
                i += 1
                continue
            
            roman += nums[i][0]
            num -= nums[i][1]

        return roman