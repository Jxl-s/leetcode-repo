directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        distances = [[float('inf')] * n for _ in range(m)]
        distances[0][0] = 0

        # i, j, cost, do 0-1 bfs
        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            cost = distances[i][j]

            for k, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue

                # if it's the correct direction
                if k + 1 == grid[i][j]:
                    if cost >= distances[ni][nj]:
                        continue

                    distances[ni][nj] = cost
                    queue.appendleft((ni, nj))
                else:
                    if cost + 1 >= distances[ni][nj]:
                        continue

                    distances[ni][nj] = cost + 1
                    queue.append((ni, nj))

        return distances[m - 1][n - 1]