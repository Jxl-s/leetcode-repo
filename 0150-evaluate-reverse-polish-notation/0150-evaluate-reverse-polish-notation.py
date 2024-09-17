class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n1 + n2)
            elif t == '-':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 - n2)
            elif t == '/':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(int(n1 / n2))
            elif t == '*':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 * n2)
            else:
                stack.append(int(t))
        
        return stack[0]