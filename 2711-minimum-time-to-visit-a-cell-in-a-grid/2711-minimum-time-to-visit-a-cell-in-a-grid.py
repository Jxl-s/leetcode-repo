class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)]

        while heap:
            time, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue

            visited[i][j] = True

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n or visited[ni][nj]:
                    continue

                delay = 1
                # if can't do one step, move between 2 nodes until it reaches time
                if time + delay < grid[ni][nj]:
                    # that caused floating point error:
                    # delay = ceil((grid[ni][nj] - time) / 2) * 2 + 1
                    delay = grid[ni][nj] - time
                    if delay % 2 == 0:
                        delay += 1

                if ni == m - 1 and nj == n - 1:
                    return time + delay

                heapq.heappush(heap, (time + delay, ni, nj))

        return -1