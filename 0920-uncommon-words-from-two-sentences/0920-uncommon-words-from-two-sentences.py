class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = Counter(s1.split(' ')) + Counter(s2.split(' '))
        output = []
        for word, count in result.items():
            if count == 1:
                output.append(word)
        
        return output