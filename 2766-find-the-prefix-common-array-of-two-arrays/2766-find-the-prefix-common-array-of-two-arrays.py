class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0] * n

        a = 0
        b = 0

        current = 0
        for i in range(n):
            a |= (1 << (A[i] - 1))
            b |= (1 << (B[i] - 1))

            if A[i] == B[i]:
                current += 1
            else:
                if (a >> (B[i] - 1)) & 1:
                    current += 1
                
                if (b >> (A[i] - 1)) & 1:
                    current += 1

            answer[i] = current

        return answer