# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([(root, 0)])

        all_sums = []
        current_sum = 0
        current_level = 0

        while len(queue) > 0:
            node, level = queue.popleft()
            if level == current_level:
                current_sum += node.val
            else:
                heapq.heappush(all_sums, current_sum)
                if len(all_sums) > k:
                    heapq.heappop(all_sums)
                
                current_sum = node.val
                current_level = level
            
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        if current_level < k - 1:
            return -1

        heapq.heappush(all_sums, current_sum)
        if len(all_sums) > k:
            heapq.heappop(all_sums)

        return all_sums[0]