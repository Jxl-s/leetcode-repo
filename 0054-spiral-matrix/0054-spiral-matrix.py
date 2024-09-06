class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1 or n == 1:
            return [a for arr in matrix for a in arr]

        wall_top, wall_bottom = 0, len(matrix)
        wall_left, wall_right = -1, len(matrix[0])

        i, j = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        output = []
        while len(output) < m * n:
            output.append(matrix[i][j])
            di, dj = directions[direction]

            i += di
            j += dj

            if direction == 0 and j + 1 == wall_right:
                wall_right -= 1
                direction = 1
            elif direction == 1 and i + 1 == wall_bottom:
                wall_bottom -= 1
                direction = 2
            elif direction == 2 and j - 1 == wall_left:
                wall_left += 1
                direction = 3
            elif direction == 3 and i - 1 == wall_top:
                wall_top += 1
                direction = 0

        return output