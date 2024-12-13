class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // n][mid % n]

            if value == target:
                return True

            if target < value:
                right = mid - 1
            else:
                left = mid + 1

        return False