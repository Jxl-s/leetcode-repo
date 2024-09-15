class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = 0
        max_count = 0

        i = 0
        j = k - 1

        for a in range(i, j + 1):
            if s[a] in vowels:
                count += 1

        max_count = count
        while j < len(s):
            if s[i] in vowels:
                count -= 1
            
            i += 1
            j += 1

            if j < len(s) and s[j] in vowels:
                count += 1
            
            max_count = max(max_count, count)
        
        return max_count