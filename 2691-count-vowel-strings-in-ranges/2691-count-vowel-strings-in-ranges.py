class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' else 0)

        return [prefix[b + 1] - prefix[a] for a, b in queries]