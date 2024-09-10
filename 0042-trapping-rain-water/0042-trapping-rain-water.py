class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        total = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] > max_left:
                    max_left = height[i]
                else:
                    total += max_left - height[i]
                    
                i += 1
            else:
                if height[j] > max_right:
                    max_right = height[j]
                else:
                    total += max_right - height[j]
                    
                j -= 1
        
        return total