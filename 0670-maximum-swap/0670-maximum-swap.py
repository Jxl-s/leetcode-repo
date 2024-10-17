class Solution:
    def maximumSwap(self, num: int) -> int:
        as_str = str(num)
        max_num = num

        for i in range(len(as_str)):
            for j in range(i + 1, len(as_str)):
                max_num = max(max_num, int(as_str[:i] + as_str[j] + as_str[i+1:j] + as_str[i] + as_str[j+1:]))

        return max_num