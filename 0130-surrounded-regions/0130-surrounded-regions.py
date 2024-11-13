class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Marking cells as edge cells
        def dfs(i, j):
            board[i][j] = 'E'
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue

                if board[ni][nj] == 'O':
                    dfs(ni, nj)
        
        # Fill cells with placeholder
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)

            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        # Surrounding them
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'E':
                    board[i][j] = 'O'