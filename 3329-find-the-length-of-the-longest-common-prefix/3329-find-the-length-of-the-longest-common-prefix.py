class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for num in arr1:
            root = trie
            for c in str(num):
                if c in root:
                    root = root[c]
                else:
                    root[c] = {}
                    root = root[c]
        
        max_len = 0
        for num in arr2:
            root = trie
            cur_len = 0

            for c in str(num):
                if c in root:
                    root = root[c]
                    cur_len += 1
                else:
                    break
            
            max_len = max(max_len, cur_len)

        return max_len