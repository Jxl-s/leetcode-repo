class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1

        while j >= 0 and s[j] == ' ':
            j -= 1

        i = j
        while i >= 0 and s[i] != ' ':
            i -= 1

        return j - i