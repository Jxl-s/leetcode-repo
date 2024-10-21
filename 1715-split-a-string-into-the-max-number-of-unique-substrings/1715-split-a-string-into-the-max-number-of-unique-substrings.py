class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()

        def backtrack(i):
            if i == len(s):
                return 0

            count = 0
            for j in range(i + 1, len(s) + 1):
                sliced = s[i:j]
                if sliced in visited:
                    continue

                visited.add(sliced)
                count = max(count, 1 + backtrack(j))
                visited.remove(sliced)

            return count
        
        return backtrack(0)