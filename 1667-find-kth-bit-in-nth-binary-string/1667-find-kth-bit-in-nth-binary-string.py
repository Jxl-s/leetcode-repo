class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(n):
            result = ""
            for c in n:
                if c == '1':
                    result += '0'
                else:
                    result += '1'
            
            return result

        def make_string(n):
            if n == 1:
                return '0'

            prev = make_string(n - 1)
            return prev + "1" + invert(prev)[::-1]
        
        return make_string(n)[k - 1]