class Solution:
    def compressedString(self, word: str) -> str:
        word += ' '

        prev = word[0]
        count = 1
        output = ''

        for i in range(1, len(word)):
            if prev == word[i]:
                count += 1
            else:
                while count > 9:
                    output += '9' + prev
                    count -= 9

                output += str(count) + prev

                prev = word[i]
                count = 1

        return output