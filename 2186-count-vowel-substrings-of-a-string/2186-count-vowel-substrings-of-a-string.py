class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        last_vowels = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
        last_consonant = -1

        count = 0
        for i, c in enumerate(word):
            if c in last_vowels:
                last_vowels[c] = i
                count += max(min(last_vowels.values()) - last_consonant, 0)
            else:
                last_consonant = i

        return count