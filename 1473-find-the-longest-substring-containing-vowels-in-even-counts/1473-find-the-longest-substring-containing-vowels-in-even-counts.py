class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        prefix = {0: -1}

        max_len = 0
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= (1 << vowels[s[i]])
            
            if mask in prefix:
                max_len = max(max_len, i - prefix[mask])
            else:
                prefix[mask] = i

        return max_len