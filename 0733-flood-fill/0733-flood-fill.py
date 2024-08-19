class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        visited = set()
        def visit(y, x):
            if y >= len(image) or y < 0:
                return
            
            if x >= len(image[0]) or x < 0:
                return

            if (y, x) in visited:
                return

            visited.add((y, x))
            if image[y][x] == start_color:
                image[y][x] = color

                visit(y + 1, x)
                visit(y - 1, x)
                visit(y, x + 1)
                visit(y, x - 1)

        visit(sr, sc)
        return image