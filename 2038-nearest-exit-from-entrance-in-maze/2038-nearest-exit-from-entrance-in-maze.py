class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def is_edge(i, j):
            if i == entrance[0] and j == entrance[1]:
                return False

            if i == 0 or j == 0:
                return True
            
            if i == m - 1 or j == n - 1:
                return True
            
            return False

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(queue) > 0:
            i, j, steps = queue.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                if maze[ni][nj] == '.':
                    if is_edge(ni, nj):
                        return steps + 1

                    maze[ni][nj] = '+'
                    queue.append((ni, nj, steps + 1))

        return -1