class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        target = Counter(t)
        current = Counter()

        i = 0
        shortest = s
        found = False

        for j in range(len(s)):
            current[s[j]] += 1

            while current >= target:
                sliced = s[i:j+1]
                found = True
                if len(sliced) < len(shortest):
                    shortest = sliced

                current[s[i]] -= 1
                i += 1
        
        if not found:
            return ''
        
        return shortest