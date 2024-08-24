class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(options, current):
            if len(options) == 0:
                return [current]

            sub = []
            for i in range(len(options)):
                opt = options[i]

                copy = current[:]
                copy.append(opt)

                new_opts = options[:i] + options[i+1:]
                sub.extend(dfs(new_opts, copy))

            return sub

        return dfs(nums, [])