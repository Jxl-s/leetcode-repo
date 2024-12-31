class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def trie_add(word):
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}

                root = root[c]

            root['.'] = word

        def trie_del(node, word, depth=0):
            if depth == len(word):
                del node['.']
                return None if len(node) == 0 else node

            node[word[depth]] = trie_del(node[word[depth]], word, depth + 1)
            if node[word[depth]] is None:
                del node[word[depth]]

            return None if len(node) == 0 else node

        for word in words:
            trie_add(word)

        output = []
        visited = [[False] * n for _ in range(m)]

        def backtrack(node, i, j):
            if visited[i][j]:
                return

            visited[i][j] = True
            if '.' in node:
                output.append(node['.'])
                trie_del(trie, node['.'])

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                
                if board[ni][nj] in node:
                    backtrack(node[board[ni][nj]], ni, nj)

            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(trie[board[i][j]], i, j)

        return output