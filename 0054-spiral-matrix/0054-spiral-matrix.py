class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return [item for sub_list in matrix for item in sub_list]

        i, j = 0, 0
        direction = 0

        # top right bottom left
        walls = [-1, len(matrix[0]), len(matrix), -1]

        arr = []
        while len(arr) < len(matrix) * len(matrix[0]):
            arr.append(matrix[i][j])

            if direction == 0:
                j += 1
                if j == walls[1] - 1:
                    direction = 1
                    walls[0] += 1
            elif direction == 1:
                i += 1
                if i == walls[2] - 1:
                    direction = 2
                    walls[1] -= 1
            elif direction == 2:
                j -= 1
                if j == walls[3] + 1:
                    direction = 3
                    walls[2] -= 1
            elif direction == 3:
                i -= 1
                if i == walls[0] + 1:
                    direction = 0
                    walls[3] += 1

        return arr