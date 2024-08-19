class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        memory = []
        for token in tokens:
            if token == '+':
                memory.append(memory.pop() + memory.pop())
            elif token == '*':
                memory.append(memory.pop() * memory.pop())
            elif token == '/':
                num_2 = memory.pop()
                num_1 = memory.pop()

                memory.append(math.trunc(num_1 / num_2))
            elif token == '-':
                num_2 = memory.pop()
                num_1 = memory.pop()

                memory.append(num_1 - num_2)
            else:
                memory.append(int(token))

        return memory[0]