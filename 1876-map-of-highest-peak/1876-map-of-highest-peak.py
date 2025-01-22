directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))

                # will be -1 for land (unexplored), and 0 for water
                isWater[i][j] -= 1

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                if isWater[ni][nj] != -1:
                    continue

                isWater[ni][nj] = isWater[i][j] + 1
                queue.append((ni, nj))

        return isWater