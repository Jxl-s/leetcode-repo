class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        options = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]

        selections = []
        

        for digit in digits:
            selections.append(options[int(digit)])

        output = []
        stack = []

        for letter in selections[0]:
            stack.append([letter])

        while len(stack) > 0:
            path = stack.pop()
            if len(path) == len(selections):
                output.append(''.join(path))
            else:
                next_arr = selections[len(path)]
                for char in next_arr:
                    stack.append([*path, char])

        return output