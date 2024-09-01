class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        output = [[0] * n for _ in range(m)]
        for x in range(len(original)):
            i = x // n
            j = x % n
            output[i][j] = original[x]

        return output