class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        counter_1 = Counter(word1)
        counter_2 = Counter(word2)

        return sorted(counter_1.values()) == sorted(counter_2.values())