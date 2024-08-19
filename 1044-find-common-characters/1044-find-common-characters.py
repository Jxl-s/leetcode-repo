class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        last_seen = Counter(words[0])
        for i in range(1, len(words)):
            counts = Counter(words[i])
            to_remove = set()

            for char, count in last_seen.items():
                if char not in counts:
                    to_remove.add(char)
                else:
                    last_seen[char] = min(last_seen[char], counts[char])

            for char in to_remove:
                del last_seen[char]

        output = []
        for char, count in last_seen.items():
            for i in range(count):
                output.append(char)
        
        return output