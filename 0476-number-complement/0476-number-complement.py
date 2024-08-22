class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join(['1' if a == '0' else '0' for a in bin(num)[2:]]), 2)