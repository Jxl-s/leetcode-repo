# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dp(i, j):
            if i > j:
                return [None]

            if i == j:
                return [TreeNode(i)]

            answer = []
            for root in range(i, j + 1):
                left, right = dp(i, root - 1), dp(root + 1, j)

                for left_node in left:
                    for right_node in right:
                        answer.append(TreeNode(root, left_node, right_node))

            return answer

        return dp(1, n)