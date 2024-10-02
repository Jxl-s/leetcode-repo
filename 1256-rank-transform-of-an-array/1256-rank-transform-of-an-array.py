class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))

        ranks = {}
        for i, r in enumerate(a):
            ranks[r] = i + 1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr