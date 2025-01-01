class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        updates = []
        for i in range(m):
            for j in range(n):
                neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < 0 or nj < 0 or ni >= m or nj >= n:
                        continue
                    
                    if board[ni][nj] == 1:
                        neighbors += 1
                
                if board[i][j] == 1:
                    # 1 and 3
                    if neighbors < 2 or neighbors > 3:
                        updates.append((i, j, 0))

                if board[i][j] == 0 and neighbors == 3:
                    updates.append((i, j, 1))
        
        for i, j, state in updates:
            board[i][j] = state