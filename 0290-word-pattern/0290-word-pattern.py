class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = defaultdict(str)
        used = set()

        split = s.split(' ')
        if len(pattern) != len(split):
            return False

        for c, x in zip(pattern, split):
            if c not in patterns:
                if x in used:
                    return False

                used.add(x)
                patterns[c] = x

            if x != patterns[c]:
                return False

        return True