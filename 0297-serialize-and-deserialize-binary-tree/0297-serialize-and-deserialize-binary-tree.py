# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        id = 0
        output = ''

        def dfs(node, parent_id, side):
            nonlocal id, output
            id += 1
            new_id = id
            output += str(parent_id) + ';' + str(new_id) + ';' + str(node.val) + ';' + side + '|'

            if node.left:
                dfs(node.left, new_id, 'l')
            if node.right:
                dfs(node.right, new_id, 'r')
        
        if root:
            dfs(root, 0, '')
        
        print(output)
        return output

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # parent_id, node_id, node_val, side
        nodes = {}
        root = None

        for node_data in data.split('|'):
            if node_data == '':
                continue

            parent_id, node_id, node_val, side = node_data.split(';')

            parent_id = int(parent_id)
            node_id = int(node_id)
            node_val = int(node_val)

            nodes[node_id] = TreeNode(node_val)
            if side == 'l':
                nodes[parent_id].left = nodes[node_id]
            elif side == 'r':
                nodes[parent_id].right = nodes[node_id]
            else:
                root = nodes[node_id]

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))