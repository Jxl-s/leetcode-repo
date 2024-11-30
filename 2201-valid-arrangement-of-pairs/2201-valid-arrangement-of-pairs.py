class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        degree = defaultdict(int)

        for a, b in pairs:
            adj[a].append(b)
            degree[a] += 1
            degree[b] -= 1

        def euler(node, output=[]):
            while len(adj[node]) > 0:
                euler(adj[node].pop(), output)

            output.append(node)
            return output[::-1]

        # Find start euler node
        start = None
        for node in adj.keys():
            if degree[node] == 1:
                start = node
                break
        
        # Not found, use any with an edge
        if start is None:
            for node in adj.keys():
                if len(adj[node]) > 0:
                    start = node
                    break

        circuit = euler(start)
        answer = []

        for i in range(1, len(circuit)):
            answer.append([circuit[i - 1], circuit[i]])
        
        return answer