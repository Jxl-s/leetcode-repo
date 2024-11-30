class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        degree = defaultdict(int) # out degree - in degree

        for a, b in pairs:
            adj[a].append(b)
            degree[a] += 1
            degree[b] -= 1

        def euler(node):
            stack = [node]
            circuit = []

            while stack:
                top = stack[-1]
                if len(adj[top]) > 0:
                    stack.append(adj[top].pop())
                else:
                    circuit.append(stack.pop())

            return circuit[::-1]

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