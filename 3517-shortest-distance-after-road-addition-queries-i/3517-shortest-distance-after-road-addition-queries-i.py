class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[i - 1].append(i)

        answer = []
        distances = list(range(n))

        for u, v in queries:
            adj[u].append(v)
            distances[v] = min(distances[v], distances[u] + 1)
            heap = [(distances[v], v)]

            while heap:
                cur, node = heapq.heappop(heap)
                if cur > distances[node]:
                    continue

                for neighbor in adj[node]:
                    new_dist = cur + 1
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))

            answer.append(distances[-1])
        
        return answer