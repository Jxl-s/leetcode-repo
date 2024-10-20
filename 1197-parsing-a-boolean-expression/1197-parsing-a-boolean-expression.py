class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operators = '!&|'

        stack = []
        current = ''

        for c in expression:
            if c in operators:
                symbol = c
            elif c == '(':
                stack.append((symbol, current))
                symbol, current = '', ''
            elif c == ')':
                prev_symbol, prev_expression = stack.pop()
                result = 't'

                if prev_symbol == '&' and 'f' in current:
                    result = 'f'
                
                if prev_symbol == '|' and 't' not in current:
                    result = 'f'

                if prev_symbol == '!' and current == 't':
                    result = 'f'

                current = prev_expression + result
            else:
                current += c

        return current == 't'