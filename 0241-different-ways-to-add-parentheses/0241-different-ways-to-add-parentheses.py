class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def dp(exp):
            if exp in memo:
                return memo[exp]

            if exp.isdigit():
                memo[exp] = [int(exp)]
                return memo[exp]
            
            output = []
            for i in range(len(exp)):
                if exp[i] in '-+*':
                    left = dp(exp[:i])
                    right = dp(exp[i+1:])

                    for l in left:
                        for r in right:
                            if exp[i] == '-':
                                output.append(l - r)
                            elif exp[i] == '+':
                                output.append(l + r)
                            elif exp[i] == '*':
                                output.append(l * r)

            memo[exp] = output
            return output

        return dp(expression)