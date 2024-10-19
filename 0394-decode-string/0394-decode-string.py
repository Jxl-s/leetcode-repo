class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        output = ''
        count = 0

        for c in s:
            if c.isdigit():
                count = count * 10 + int(c)
            elif c == '[':
                stack.append((output, count))
                output = ''
                count = 0
            elif c == ']':
                previous, n = stack.pop()
                output = previous + output * n
            else:
                output += c
        
        return output