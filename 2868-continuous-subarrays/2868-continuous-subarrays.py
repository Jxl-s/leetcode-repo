class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = 0
        count = 0

        min_queue = deque()
        max_queue = deque()

        for j in range(len(nums)):
            # Fix queue
            while min_queue and nums[min_queue[-1]] >= nums[j]:
                min_queue.pop()

            while max_queue and nums[max_queue[-1]] <= nums[j]:
                max_queue.pop()
            
            min_queue.append(j)
            max_queue.append(j)

            while nums[max_queue[0]] - nums[min_queue[0]] > 2:
                i += 1

                # Remove items not in the subarray
                while i > max_queue[0]:
                    max_queue.popleft()

                while i > min_queue[0]:
                    min_queue.popleft()

            count += j - i + 1

        return count