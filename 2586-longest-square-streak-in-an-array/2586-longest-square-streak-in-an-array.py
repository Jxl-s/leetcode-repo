class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = -1

        for num in nums:
            streak = 1
            current = num

            while True:
                current = current ** 2
                if current in nums:
                    streak += 1
                else:
                    break
            
            if streak == 1:
                streak = -1

            max_streak = max(max_streak, streak)

        return max_streak
