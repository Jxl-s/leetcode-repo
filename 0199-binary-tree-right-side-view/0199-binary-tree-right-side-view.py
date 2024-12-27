# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        view = []
        queue = deque([root])
        while queue:
            last = -1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                last = node.val
            
            view.append(last)
        
        return view