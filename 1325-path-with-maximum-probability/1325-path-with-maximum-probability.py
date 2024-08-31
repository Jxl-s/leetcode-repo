class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for i in range(n)]

        for i in range(len(edges)):
            a, b = edges[i]
            w = succProb[i]

            adj[a].append((b, w))
            adj[b].append((a, w))

        visited = {}
        heap = [(-1, start_node)]

        while len(heap) > 0:
            w, node = heappop(heap)
            w = -w
            if node in visited:
                continue

            visited[node] = w
            if node == end_node:
                return w

            for n2, w2 in adj[node]:
                if n2 not in visited:
                    heappush(heap, (-w * w2, n2))

        return 0