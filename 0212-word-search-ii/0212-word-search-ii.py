class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        trie = {}
        for w in words:
            root = trie
            for c in w:
                if c not in root:
                    root[c] = {}

                root = root[c]

            root['.'] = w

        output = []
        visited = [[False] * n for i in range(m)]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j, root):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if visited[i][j]:
                return
            
            visited[i][j] = True
            if board[i][j] in root:
                if '.' in root[board[i][j]]:
                    output.append(root[board[i][j]]['.'])

                for di, dj in directions:
                    dfs(i + di, j + dj, root[board[i][j]])
            
            visited[i][j] = False
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return output