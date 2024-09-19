class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            cur = expression[i:j+1]
            if cur.isdigit():
                memo[(i, j)] = [int(cur)]
                return memo[(i, j)]

            output = []            
            for k in range(i, j + 1):
                if expression[k] in '+-*':
                    left = dp(i, k - 1)
                    right = dp(k + 1, j)

                    for l in left:
                        for r in right:
                            if expression[k] == '+':
                                output.append(l + r)
                            elif expression[k] == '-':
                                output.append(l - r)
                            elif expression[k] == '*':
                                output.append(l * r)

            memo[(i, j)] = output
            return output
        
        return dp(0, len(expression) - 1)