class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        cur = pref[0]
        output = [0] * len(pref)
        output[0] = pref[0]

        for i in range(1, len(pref)):
            output[i] = cur ^ pref[i]
            cur = pref[i]

        return output