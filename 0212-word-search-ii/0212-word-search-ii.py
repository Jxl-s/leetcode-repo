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
            item = board[i][j]
            if visited[i][j]:
                return

            visited[i][j] = True
            if '.' in root[item]:
                word = root[item]['.']

                output.append(word)
                del root[item]['.']

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and board[ni][nj] in root[item]:
                    dfs(ni, nj, root[item])

            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return output