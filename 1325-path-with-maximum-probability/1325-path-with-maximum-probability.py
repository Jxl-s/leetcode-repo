class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for i in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]

            adj[a].append((b, prob))
            adj[b].append((a, prob))

        heap = [(-1, start_node)]
        max_prob = [0] * n
        max_prob[start_node] = 1

        while len(heap) > 0:
            cur_prob, cur_node = heappop(heap)
            cur_prob = -cur_prob

            if cur_node == end_node:
                return cur_prob

            for neighbor_node, neighbor_prob in adj[cur_node]:
                new_prob = cur_prob * neighbor_prob
                if new_prob > max_prob[neighbor_node]:
                    max_prob[neighbor_node] = new_prob
                    heappush(heap, (-new_prob, neighbor_node))

        return 0