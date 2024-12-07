class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        distances = [float('inf')] * n
        distances[k - 1] = 0

        heap = [(0, k)]
        while len(heap) > 0:
            time, node = heapq.heappop(heap)
            if time > distances[node - 1]:
                continue

            for neighbor, weight in adj[node]:
                new_time = time + weight
                if new_time >= distances[neighbor - 1]:
                    continue
                
                distances[neighbor - 1] = new_time
                heapq.heappush(heap, (new_time, neighbor))

        result = max(distances)
        return -1 if result == float('inf') else result