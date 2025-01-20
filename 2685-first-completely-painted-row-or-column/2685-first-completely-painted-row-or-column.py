class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        indexes = [0] * len(arr)
        rows, cols = [n] * m, [m] * n

        for i in range(m):
            for j in range(n):
                indexes[mat[i][j] - 1] = (i, j)
        
        for k in range(len(arr)):
            i, j = indexes[arr[k] - 1]
            rows[i] -= 1
            cols[j] -= 1

            if rows[i] == 0: return k
            if cols[j] == 0: return k