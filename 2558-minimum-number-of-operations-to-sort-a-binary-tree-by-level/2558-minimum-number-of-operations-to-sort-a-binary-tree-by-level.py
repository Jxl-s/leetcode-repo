# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        targets = []

        while queue:
            values = []
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                values.append(node.val)

            level_indexes = { x: i for i, x in enumerate(sorted(values)) }
            level_targets = [level_indexes[values[i]] for i in range(n)]

            prefix = len(targets)
            for i in range(n):
                targets.append(prefix + level_targets[i])

        n = len(targets)
        visited = [False] * n 
        count = 0

        def dfs(node):
            nonlocal count

            if visited[node] or visited[targets[node]] or targets[node] == node:
                return
            
            count += 1
            visited[node] = True
            dfs(targets[node])
        
        for i in range(n):
            dfs(i)

        return count