class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[False] * n for _ in range(n)]
        for i in range(1, n):
            adj[i - 1][i] = True
        
        answer = []
        distances = list(range(n))

        for u, v in queries:
            adj[u][v] = True
            distances[v] = min(distances[v], distances[u] + 1)

            # stuff after added road recalculate
            heap = [(distances[v], v)]
            while len(heap) > 0:
                distance, node = heapq.heappop(heap)
                if distance > distances[node]:
                    continue
                
                for i in range(n):
                    if not adj[node][i]:
                        continue
                    
                    if distance + 1 < distances[i]:
                        heapq.heappush(heap, (distance + 1, i))
                        distances[i] = distance + 1

            answer.append(distances[-1])

        return answer