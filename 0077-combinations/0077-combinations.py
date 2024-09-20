class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        output = []

        def backtrack(i):
            if len(current) == k:
                output.append(current[:])
                return
            
            if i > n:
                return
            
            current.append(i)
            backtrack(i + 1)
            current.pop()
            backtrack(i + 1)

        backtrack(1)
        return output