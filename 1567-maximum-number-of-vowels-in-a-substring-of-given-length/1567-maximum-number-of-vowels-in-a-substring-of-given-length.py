class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        max_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1
        
        cur_vowels = max_vowels
        for i in range(len(s) - k):
            if s[i + k] in vowels:
                cur_vowels += 1

            if s[i] in vowels:
                cur_vowels -= 1
            
            max_vowels = max(max_vowels, cur_vowels)
        
        return max_vowels