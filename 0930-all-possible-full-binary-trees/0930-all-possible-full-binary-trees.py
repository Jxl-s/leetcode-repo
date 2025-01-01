# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        @cache
        def dp(k):
            if k == 1:
                return [TreeNode()]

            answer = []
            for i in range(1, k, 2):
                left = dp(i)
                right = dp(k - i - 1)

                for left_node in left:
                    for right_node in right:
                        answer.append(TreeNode(0, left_node, right_node))

            return answer

        return dp(n)