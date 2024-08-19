class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and columns
        size = len(board)

        for i in range(size):
            seen_row = set()
            seen_col = set()

            for j in range(size):
                if board[i][j] in seen_row:
                    return False
                
                if board[j][i] in seen_col:
                    return False
                
                if board[i][j] != '.':
                    seen_row.add(board[i][j])
                
                if board[j][i] != '.':
                    seen_col.add(board[j][i])

        # check squares
        for s in range(size):
            offset_x = (s % 3) * 3
            offset_y = (s // 3) * 3

            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[i + offset_y][j + offset_x] in seen:
                        return False
                    
                    if board[i + offset_y][j + offset_x] != '.':
                        seen.add(board[i + offset_y][j + offset_x])

        return True