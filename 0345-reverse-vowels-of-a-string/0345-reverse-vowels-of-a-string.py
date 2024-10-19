class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels += [a.upper() for a in vowels]

        arr = []
        for c in s:
            if c in vowels:
                arr.append(c)
        
        output = ''
        for c in s:
            if c in vowels:
                output += arr.pop()
            else:
                output += c
        
        return output