class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        traversal = []
        reverse_diag = False

        # 1. Start with the left side
        starts = []
        for x in range(m):
            starts.append((x, 0))

        for x in range(1, n):
            starts.append((m - 1, x))

        for i, j in starts:
            diagonal = []
            while i >= 0 and i < m and j >= 0 and j < n:
                diagonal.append(mat[i][j])
                i -= 1
                j += 1

            if reverse_diag:
                diagonal = diagonal[::-1]
            
            for k in diagonal:
                traversal.append(k)

            reverse_diag = not reverse_diag

        return traversal