# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(tree_node, list_node):
            if not list_node:
                return True
            
            if not tree_node:
                return False

            if tree_node.val != list_node.val:
                return False

            if dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next):
                return True
            
            return False
        
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)