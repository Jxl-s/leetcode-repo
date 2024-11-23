class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Count number of rocks preceding obstable/wall
        m, n = len(box), len(box[0])

        for i in range(m):
            count = 0
            for j in range(n):
                if box[i][j] == '#':
                    count += 1
                    box[i][j] = '.'
                elif box[i][j] == '*':
                    for k in range(j - count, j):
                        box[i][k] = '#'

                    count = 0
            
            for j in range(n - 1, n - 1 - count, -1):
                box[i][j] = '#'

        rotated = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][i] = box[i][j]
        
        for i in range(n):
            left = 0
            right = len(rotated[i]) - 1

            while left < right:
                rotated[i][left], rotated[i][right] = rotated[i][right], rotated[i][left]
                left += 1
                right -= 1
        
        return rotated