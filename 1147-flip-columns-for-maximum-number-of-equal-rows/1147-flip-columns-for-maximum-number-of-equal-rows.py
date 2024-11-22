class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = defaultdict(int)
        for row in matrix:
            counts[tuple(row[0] ^ a for a in row)] += 1

        return max(counts.values())