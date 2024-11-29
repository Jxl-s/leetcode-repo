class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        distances = [[float('inf')] * n for _ in range(m)]
        distances[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            time, i, j = heapq.heappop(heap)
            if time > distances[i][j]:
                continue

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue

                delay = 1
                # if can't do one step, move between 2 nodes until it reaches time
                if time + delay < grid[ni][nj]:
                    # that caused floating point error:
                    # delay = ceil((grid[ni][nj] - time) / 2) * 2 + 1
                    delay = grid[ni][nj] - time
                    if delay % 2 == 0:
                        delay += 1

                if time + delay >= distances[ni][nj]:
                    continue

                if ni == m - 1 and nj == n - 1:
                    return time + delay

                distances[ni][nj] = time + delay
                heapq.heappush(heap, (time + delay, ni, nj))

        return -1