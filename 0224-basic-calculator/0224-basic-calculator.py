class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        stack = []
        segment = ''

        # Remove parenthesis
        for c in s:
            if c == '(':
                stack.append(segment)
                segment = ''
            elif c == ')':
                prefix = stack.pop()
                if prefix and prefix[-1] == '-':
                    segment = segment.replace('+', '|')
                    segment = segment.replace('-', '+')
                    segment = segment.replace('|', '-')

                segment = prefix + segment
            else:
                segment += c

        splitted = []
        operations = ['+']

        for chunk in segment.split('+'):
            for sub_chunk in chunk.split('-'):
                if not sub_chunk:
                    splitted.append(0)
                else:
                    splitted.append(int(sub_chunk))
        
        for c in segment:
            if c in '+-':
                operations.append(c)

        result = 0
        for i in range(len(splitted)):
            if operations[i] == '+':
                result += splitted[i]
            else:
                result -= splitted[i]

        return result