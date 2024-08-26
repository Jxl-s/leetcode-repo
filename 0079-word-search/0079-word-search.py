class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = [c for c in word]
        m = len(board)
        n = len(board[0])

        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(remaining, i, j):
            if i < 0 or i >= m:
                return False
            
            if j < 0 or j >= n:
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != remaining[0]:
                return False

            copy = remaining[1:]
            if len(copy) == 0:
                return True

            visited.add((i, j))

            for x, y in directions:
                if dfs(copy, i + y, j + x):
                    visited.remove((i, j))
                    return True

            visited.remove((i, j))
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(stack, i, j):
                    return True

        return False