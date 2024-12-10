class Solution:
    def maximumLength(self, s: str) -> int:
        i = 0
        j = 0

        counter = defaultdict(int)
        while i < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1

            for k in range(1, j - i + 1):
                counter[s[i] * k] += j - i - k + 1

            i = j

        longest = -1
        for key, value in counter.items():
            if value >= 3:
                longest = max(longest, len(key))

        return longest