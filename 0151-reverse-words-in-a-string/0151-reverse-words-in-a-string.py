class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        buffer = ''
        s = s.strip()

        for c in s:
            if c == ' ':
                if buffer != '':
                    output.append(buffer)
                    buffer = ''
            else:
                buffer += c
        
        output.append(buffer)
        return ' '.join(output[::-1])