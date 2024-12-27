class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Queen positions
        grid = [['.'] * n for _ in range(n)]

        # Efficient search
        rows = [False] * n
        cols = [False] * n

        diag_1 = [False] * (2 * n - 1)
        diag_2 = [False] * (2 * n - 1)

        output = []
        def addOutput():
            arr = []
            for row in grid:
                arr.append(''.join(row))

            output.append(arr)

        def canPlace(i, j):
            # Rows & columns
            if rows[i]: return False
            if cols[j]: return False

            # Diagonals
            if diag_1[i + j]: return False
            if diag_2[i + n - j - 1]: return False

            return True
        
        def _setQueen(i, j, willSet):
            grid[i][j] = 'Q' if willSet else '.'

            # Rows & columns
            rows[i] = willSet
            cols[j] = willSet

            # Diagonals
            diag_1[i + j] = willSet
            diag_2[i + n - j - 1] = willSet

        placeQueen = lambda i, j: _setQueen(i, j, True)
        removeQueen = lambda i, j: _setQueen(i, j, False)

        # x is the x'th queen (at row x)
        def backtrack(x):
            if x == n:
                addOutput()
                return

            for j in range(n):
                # try finding a spot on this row
                if not canPlace(x, j):
                    continue

                placeQueen(x, j)
                backtrack(x + 1)
                removeQueen(x, j)

        backtrack(0)
        return output