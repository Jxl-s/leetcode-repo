class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left = 0
        right = m - 1
        row = -1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                row = mid
                break

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
        
        if row == -1:
            return False
        
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
        
        return False