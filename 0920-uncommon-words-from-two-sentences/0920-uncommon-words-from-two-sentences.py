class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [word for word, count in (Counter(s1.split(' ')) + Counter(s2.split(' '))).items() if count == 1]