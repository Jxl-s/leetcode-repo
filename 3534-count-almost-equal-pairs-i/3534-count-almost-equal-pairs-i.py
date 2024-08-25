class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def almost_equal(x, y):
            if x == y:
                return True

            strx, stry = str(x), str(y)
            max_len = max(len(strx), len(stry))

            strx = strx.zfill(max_len)
            stry = stry.zfill(max_len)

            i = 0
            different = []

            while i < len(strx):
                charx, chary = strx[i], stry[i]
                if charx != chary:
                    different.append((charx, chary))
                
                i += 1
            
            if len(different) != 2:
                return False

            if different[0][::-1] == different[1]:
                return True

            return False

        pair_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if almost_equal(nums[i], nums[j]):
                    pair_count += 1

        return pair_count