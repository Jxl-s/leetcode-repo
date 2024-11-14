class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        visited = set()
        def dfs(node, target, current):
            visited.add(node)
            for neighbor, value in adj[node]:
                if neighbor in visited:
                    continue

                if neighbor == target:
                    visited.remove(node)
                    return current * value

                result = dfs(neighbor, target, current * value)
                if result != -1.0:
                    visited.remove(node)
                    return result

            visited.remove(node)
            return -1.0
        
        output = []
        for a, b in queries:
            if a not in adj or b not in adj:
                output.append(-1)
                continue
            
            if a == b:
                output.append(1)
                continue

            output.append(dfs(a, b, 1))

        return output