class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rel = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for c in s:
            if c in rel:
                if len(stack) == 0:
                    return False

                if stack.pop() != rel[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0