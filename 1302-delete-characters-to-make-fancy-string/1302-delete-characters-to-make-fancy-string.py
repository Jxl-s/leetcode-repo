class Solution:
    def makeFancyString(self, s: str) -> str:
        s += ' '

        output = ''
        count, char = 1, s[0]

        for i in range(1, len(s)):
            if char == s[i]:
                count += 1
            else:
                output += min(count, 2) * char
                count, char = 1, s[i]

        return output