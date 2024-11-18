class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        prefix = [0] * (2 * n + 1)

        for i in range(2 * n):
            prefix[i + 1] = prefix[i] + code[i % n]

        output = [0] * n

        if k > 0:
            for i in range(n):
                output[i] = prefix[i + k + 1] - prefix[i + 1]

        if k < 0:
            for i in range(n):
                output[i] = prefix[i + n] - prefix[i + n + k]

        return output