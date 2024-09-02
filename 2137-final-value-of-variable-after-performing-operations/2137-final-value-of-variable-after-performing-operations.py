class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '++' in op:
                x += 1
            if '--' in op:
                x -= 1
        
        return x