class Solution:
    def compress(self, chars: List[str]) -> int:
        k = -1

        cur_c = chars[0]
        cur_count = 1

        for i in range(1, len(chars) + 1):
            c = chars[i] if i < len(chars) else ''
            if c == cur_c:
                cur_count += 1
            else:
                k += 1
                chars[k] = cur_c

                if cur_count > 1:
                    digits = []
                    while cur_count > 0:
                        digit = cur_count % 10
                        cur_count //= 10
                        digits.append(str(digit))

                    for n in digits[::-1]:
                        k += 1
                        chars[k] = n

                cur_count = 1
                cur_c = c

        return k + 1