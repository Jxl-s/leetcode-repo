class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # case: < 10
        if len(n) == 1:
            return str(int(n) - 1)
        
        # case: 100 ... 000
        if n[0] == '1' and all(c == '0' for c in n[1:]):
            return str(int(n) - 1)

        # case: 100 ... 001
        if n[0] == '1' and n[-1] == '1' and all(c == '0' for c in n[1:-1]):
            return str(int(n) - 2)
        
        # case: 999 ... 999
        if all(c == '9' for c in n):
            return str(int(n) + 2)

        half_str = n[:(len(n)+1)//2]
        lower_str = str(int(half_str) - 1)
        higher_str = str(int(half_str) + 1)

        possible = set()

        if len(n) % 2 == 0:
            possible.add(half_str + half_str[::-1])
            possible.add(lower_str + lower_str[::-1])
            possible.add(higher_str + higher_str[::-1])
        else:
            possible.add(half_str + half_str[::-1][1:])
            possible.add(lower_str + lower_str[::-1][1:])
            possible.add(higher_str + higher_str[::-1][1:])
        
        if n in possible:
            possible.remove(n)

        return min(possible, key=lambda x: (abs(int(n) - int(x)), int(x)))