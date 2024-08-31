class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for i in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]

            adj[a].append((b, prob))
            adj[b].append((a, prob))
        
        max_prob = 0
        visited = set()

        def dfs(node, prob):
            nonlocal max_prob
            if node in visited:
                return

            if node == end_node:
                max_prob = max(max_prob, prob)
                return
            
            visited.add(node)

            for child, child_prob in adj[node]:
                dfs(child, prob * child_prob)


        dfs(start_node, 1)
        return max_prob