class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stations = defaultdict(list)
        adj = defaultdict(set)

        for i, route in enumerate(routes):
            for station in route:
                for neighbor in stations[station]:
                    adj[i].add(neighbor)
                    adj[neighbor].add(i)

                stations[station].append(i)

        targets = set(stations[target])

        queue = deque()
        for station in stations[source]:
            queue.append((station, 1))

        visited = set()
        while queue:
            station, distance = queue.popleft()
            if station in targets:
                return distance

            for neighbor in adj[station]:
                if neighbor in visited:
                    continue
                
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
        
        return -1