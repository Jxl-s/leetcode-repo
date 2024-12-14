class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []

        for j in range(len(nums)):
            # Remove indices out of window
            while queue and queue[0] < j - k + 1:
                queue.popleft()

            # Make sure it's decreasing
            while queue and nums[queue[-1]] <= nums[j]:
                queue.pop()

            queue.append(j)
            if j >= k - 1:
                output.append(nums[queue[0]])

        return output