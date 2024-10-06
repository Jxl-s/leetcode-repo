class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        for i in range(n // 2):
            out.append((i+1))
            out.append(-(i+1))
        
        if n % 2 == 1:
            out.append(0)

        return out