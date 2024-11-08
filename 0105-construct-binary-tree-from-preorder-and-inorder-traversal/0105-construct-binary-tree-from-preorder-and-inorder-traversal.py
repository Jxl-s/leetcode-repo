class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: idx for idx, value in enumerate(inorder)}

        def make_node(i, start, end):
            if start > end:
                return None

            index = index_map[preorder[i]]
            root = TreeNode(preorder[i])

            root.left = make_node(i + 1, start, index - 1)
            root.right = make_node(i + (index - start) + 1, index + 1, end)

            return root

        return make_node(0, 0, len(inorder) - 1)
