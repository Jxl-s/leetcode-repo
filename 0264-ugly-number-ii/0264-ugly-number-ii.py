class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        output = [1]

        for i in range(n - 1): # n - 1 because there's already 1 item in output
            val2, val3, val5 = output[p2] * 2, output[p3] * 3, output[p5] * 5

            next = min(val2, val3, val5)
            output.append(next)

            if next == val2:
                p2 += 1

            if next == val3:
                p3 += 1

            if next == val5:
                p5 += 1

        return output[-1]