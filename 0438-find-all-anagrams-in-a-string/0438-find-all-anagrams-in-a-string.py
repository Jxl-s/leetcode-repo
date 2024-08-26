class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        counts = defaultdict(int)
        for c in p:
            counts[c] += 1
        
        i = 0
        j = len(p) - 1
        cur_counts = defaultdict(int)

        for x in range(i, j + 1):
            cur_counts[s[x]] += 1

        output = []
        while j < len(s):
            if cur_counts == counts:
                output.append(i)
            
            cur_counts[s[i]] -= 1
            if cur_counts[s[i]] <= 0:
                del cur_counts[s[i]]
            
            i += 1
            j += 1

            if j < len(s):
                cur_counts[s[j]] += 1

        return output