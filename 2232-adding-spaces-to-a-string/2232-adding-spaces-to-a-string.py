class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0 # spaces
        j = 0 # in s

        output = ''
        while i < len(spaces):
            if j == spaces[i]:
                output += ' '
                i += 1

            output += s[j]
            j += 1

        while j < len(s):
            output += s[j]
            j += 1

        return output