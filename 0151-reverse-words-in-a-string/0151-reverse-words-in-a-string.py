class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        words = s.strip().split(' ')
        for i in range(len(words) - 1, -1, -1):
            if words[i] == '':
                continue
            
            if output != '':
                output += ' ' + words[i]
            else:
                output += words[i]

        return output