class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                height = heights[index]
                width = i

                if stack:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area