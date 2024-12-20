class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for start, end in tickets:
            adj[start].append(end)
        
        for l in adj.values():
            l.sort(reverse=True)

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

        return euler('JFK')