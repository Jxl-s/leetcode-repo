class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)

        total = 0
        for count in counter.values():
            total += 1 if count % 2 == 1 else 2

        return total