# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def make_node(root, start, end):
            nonlocal i
            if start > end:
                return None

            index = inorder.index(preorder[i])
            node = TreeNode(preorder[i])
            i += 1

            node.left = make_node(node, start, index - 1)
            node.right = make_node(node, index + 1, end)

            return node
        
        index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        i += 1

        root.left = make_node(root, 0, index - 1)
        root.right = make_node(root, index + 1, len(inorder) - 1)

        return root