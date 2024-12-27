class Solution:
    def addItem(self, i, j, val):
        self.board[i][j] = str(val)

        self.row_sets[i].add(self.board[i][j])
        self.col_sets[j].add(self.board[i][j])
        self.box_sets[(i // 3) * 3 + j // 3].add(self.board[i][j])
    
    def removeItem(self, i, j):
        self.row_sets[i].remove(self.board[i][j])
        self.col_sets[j].remove(self.board[i][j])
        self.box_sets[(i // 3) * 3 + j // 3].remove(self.board[i][j])

        self.board[i][j] = '.'

    def canPlace(self, i, j, val):
        as_str = str(val)
        if as_str in self.row_sets[i]:
            return False

        if as_str in self.col_sets[j]:
            return False
        
        if as_str in self.box_sets[(i // 3) * 3 + j // 3]:
            return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row_sets = [set() for _ in range(9)]
        self.col_sets = [set() for _ in range(9)]
        self.box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                # Row and columns
                self.row_sets[i].add(board[i][j])
                self.col_sets[j].add(board[i][j])

                # Boxes
                box_no = (i // 3) * 3 + j // 3
                self.box_sets[box_no].add(board[i][j])

        options = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    options.append((i, j))

        # x is index in options
        n = len(options)
        def backtrack(x):
            i, j = options[x]
            for val in range(1, 10):
                if not self.canPlace(i, j, val):
                    continue

                self.addItem(i, j, val)
                if x == n - 1:
                    return self.board

                result = backtrack(x + 1)
                if result:
                    return result

                self.removeItem(i, j)

        return backtrack(0)