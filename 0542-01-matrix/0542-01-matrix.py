from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        output = [[-1] * len(m) for m in mat]

        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(queue) > 0:
            y, x = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(mat[0]) and ny >= 0 and ny < len(mat):
                    if output[ny][nx] == -1:
                        output[ny][nx] = output[y][x] + 1
                        queue.append((ny, nx))

        return output