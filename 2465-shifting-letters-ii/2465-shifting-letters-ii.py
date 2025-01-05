class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            prefix[start] += direction * 2 - 1
            prefix[end + 1] -= direction * 2 - 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        output = ''
        for i in range(len(prefix) - 1):
            previous = ord(s[i]) - ord('a')
            previous += prefix[i]
            previous %= 26

            output += chr(previous + ord('a'))
        
        return output