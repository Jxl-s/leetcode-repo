class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        total = 0
        negatives = 0
        min_item = float('inf')

        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= 0:
                    negatives += 1

                total += abs(matrix[i][j])
                min_item = min(min_item, abs(matrix[i][j]))
        
        if negatives % 2 == 0:
            return total
        
        return total - min_item*2