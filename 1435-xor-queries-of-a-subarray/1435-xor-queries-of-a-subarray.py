class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cur_val = arr[0]
        prefix = [cur_val]

        for i in range(1, len(arr)):
            cur_val = cur_val ^ arr[i]
            prefix.append(cur_val)

        out = []
        for a, b in queries:
            if a == 0:
                out.append(prefix[b])
            else:
                out.append(prefix[a - 1] ^ prefix[b])
        
        return out