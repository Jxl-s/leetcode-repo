class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = {}
        for f in folder:
            parts = f.split('/')[1:]
            current = root

            for p in parts:
                if p not in current:
                    current[p] = {}
                
                current = current[p]
            
            current['.'] = True

        output = []
        def dfs(path, node):
            if '.' in node:
                output.append(path)
                return
            
            for sub in node.keys():
                dfs(path + '/' + sub, node[sub])

        for sub in root.keys():
            dfs('/' + sub, root[sub])
        
        return output