class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def dfs(node, target, current, visited):
            visited.add(node)
            for neighbor, value in adj[node]:
                if neighbor in visited:
                    continue

                if neighbor == target:
                    return current * value

                result = dfs(neighbor, target, current * value, visited)
                if result != -1.0:
                    return result

            return -1.0
        
        output = []
        for a, b in queries:
            if a not in adj or b not in adj:
                output.append(-1)
                continue
            
            if a == b:
                output.append(1)
                continue

            output.append(dfs(a, b, 1, set()))

        return output