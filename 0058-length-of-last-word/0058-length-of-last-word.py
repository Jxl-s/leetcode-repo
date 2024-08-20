class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s.count(' ') == 0:
            return len(s)

        j = len(s) - 1
        i = j

        while i > 0 and s[i] != ' ':
            i -= 1

        return j - i