class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(' ')

        count = 1
        prev = chars[0]
        k = 0

        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                prev = chars[i]

                chars[k] = chars[i - 1]
                k += 1

                if count > 1:
                    for c in str(count):
                        chars[k] = c
                        k += 1

                count = 1

        return k