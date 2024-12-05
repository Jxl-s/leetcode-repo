class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        i = 0
        j = 0

        if start.replace('_', '') != target.replace('_', ''):
            return False

        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1

            while j < n and target[j] == '_':
                j += 1

            if i == n: return j == n
            if j == n: return i == n

            if start[i] != target[j]:
                return False

            if start[i] == 'L' and j > i:
                return False
            
            if start[i] == 'R' and j < i:
                return False

            i += 1
            j += 1
        
        return True