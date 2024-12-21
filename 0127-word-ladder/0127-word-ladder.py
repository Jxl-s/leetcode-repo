class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        index = {x: i for i, x in enumerate(wordList)}
        if endWord not in index:
            return 0

        n = len(wordList)

        pattern_map = defaultdict(list)
        for i, word in enumerate(wordList):
            for j in range(len(word)):
                pattern = word[:j] + '.' + word[j+1:]
                pattern_map[pattern].append(i)

        # keep track of unique entries
        adj = [set() for _ in range(n)]
        for values in pattern_map.values():
            if len(values) <= 1:
                continue

            for i in range(len(values)):
                for j in range(1, len(values)):
                    adj[values[i]].add(values[j])
                    adj[values[j]].add(values[i])

        # convert back to list
        for i in range(n):
            adj[i] = list(adj[i])
        
        # find start nodes
        start = set()
        visited = [False] * n

        for i in range(len(beginWord)):
            pattern = beginWord[:i] + '.' + beginWord[i+1:]
            for word in pattern_map[pattern]:
                start.add(word)
                visited[word] = True

        # start bfs
        queue = deque(start)

        depth = 2
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == index[endWord]:
                    return depth

                for neighbor in adj[node]:
                    if visited[neighbor]:
                        continue
                    
                    visited[neighbor] = True
                    queue.append(neighbor)

            depth += 1

        return 0