class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        word_len = len(words[0])
        target_len = len(target)

        counts = [defaultdict(int) for _ in range(word_len)]

        for word in words:
            for i in range(word_len):
                counts[i][word[i]] += 1

        @cache
        def dp(i, k):
            if i == len(target): return 1
            if k == len(words[0]): return 0

            count = dp(i, k + 1)
            char_count = counts[k][target[i]]

            if char_count > 0:
                count += char_count * dp(i + 1, k + 1)
                count %= (10**9 + 7)

            return count

        return dp(0, 0)