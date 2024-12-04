class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_char = lambda c: chr(ord('a') + (ord(c) - ord('a') + 1) % 26)

        i = 0 # in str1
        j = 0 # in str2

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or next_char(str1[i]) == str2[j]:
                j += 1

            i += 1

        return j == len(str2)