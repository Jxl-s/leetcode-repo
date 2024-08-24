class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = []

        def dfs(i, comb, remainder):
            if remainder == 0:
                copy = comb[:]
                total.append(copy)
                return
            
            for j in range(i, len(candidates)):
                if remainder - candidates[j] < 0:
                    continue
                
                copy = comb[:]
                copy.append(candidates[j])
                dfs(j, copy, remainder - candidates[j])

        dfs(0, [], target)
        return total