class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = nums[i] + prefix[i]

        shortest = float('inf')
        queue = deque()

        for j in range(n + 1):
            while len(queue) > 0 and prefix[j] - prefix[queue[0]] >= k:
                shortest = min(shortest, j - queue.popleft())

            while len(queue) > 0 and prefix[j] <= prefix[queue[-1]]:
                queue.pop()

            queue.append(j)

        return shortest if shortest != float('inf') else -1