class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def backtrack(i, j, index):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if visited[i][j]:
                return False

            visited[i][j] = True
            if board[i][j] == word[index]:
                if index + 1 == len(word):
                    return True

                for di, dj in directions:
                    if backtrack(i + di, j + dj, index + 1):
                        return True

            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False