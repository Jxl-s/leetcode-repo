class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Operation 1: Swapping characters (must use same chars)
        if set(word1) != set(word2):
            return False

        # Operation 2: Transforming (counts must be similar)
        counter_1 = Counter(word1)
        counter_2 = Counter(word2)

        return sorted(counter_1.values()) == sorted(counter_2.values())