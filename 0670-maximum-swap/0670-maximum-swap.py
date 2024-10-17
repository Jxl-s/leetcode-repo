class Solution:
    def maximumSwap(self, num: int) -> int:
        def swap(i, j):
            as_str = str(num)
            return int(as_str[:i] + as_str[j] + as_str[i+1:j] + as_str[i] + as_str[j+1:])

        max_num = num
        for i in range(len(str(num))):
            for j in range(i + 1, len(str(num))):
                max_num = max(max_num, swap(i, j))

        return max_num