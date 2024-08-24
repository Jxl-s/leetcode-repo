class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # one digit numbers
        if len(n) <= 1:
            return str(int(n) - 1)
        
        # all 9's
        if all(c == "9" for c in n):
            return str(int(n) + 2)

        # 100 ... 001
        if n[0] == "1" and n[-1] == "1" and all(c == "0" for c in n[1:-1]):
            return str(int(n) - 2)

        # 100000
        if n[0] == "1" and all(c == "0" for c in n[1:]):
            return str(int(n) - 1)

        possible = set()

        half = n[: (len(n) + 1) // 2]
        lowered = str(int(half) - 1)
        highered = str(int(half) + 1)

        # flipping normally, lowering, highering
        if len(n) % 2 == 0:
            possible.add(half + half[::-1])
            possible.add(lowered + lowered[::-1])
            possible.add(highered + highered[::-1])
        else:
            possible.add(half + half[::-1][1:])
            possible.add(lowered + lowered[::-1][1:])
            possible.add(highered + highered[::-1][1:])

        if n in possible:
            possible.remove(n)

        return min(possible, key=lambda x: (abs(int(x) - int(n)), int(x)))