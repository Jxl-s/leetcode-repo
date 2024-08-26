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
        def dfs(path):
            if len(path) == len(selections):
                output.append(path)
                return

            next_arr = selections[len(path)]
            for char in next_arr:
                copy = path[:]
                copy.append(char)

                dfs(copy)
            
        dfs([])
        return [''.join(a) for a in output]