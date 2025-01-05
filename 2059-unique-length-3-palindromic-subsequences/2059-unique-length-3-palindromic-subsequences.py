class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # first and last occurence of each char
        first = defaultdict(int)
        last = defaultdict(int)

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        
        count = 0
        for c in first.keys():
            first_occ = first[c]
            last_occ = last[c]

            if last_occ - first_occ <= 1:
                continue 

            # count unique chars within
            seen = set()
            for i in range(first_occ + 1, last_occ):
                if s[i] in seen:
                    continue
                
                seen.add(s[i])
                count += 1

        return count