class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        ord_a = ord('a')
        a1 = ord(coordinate1[0:1]) - ord('a') + 1
        b1 = int(coordinate1[1:])
        a2 = ord(coordinate2[0:1]) - ord('a') + 1
        b2 = int(coordinate2[1:])

        if (a1 + b1) % 2 == 0:
            return (a2 + b2) % 2 == 0

        return (a2 + b2) % 2 == 1