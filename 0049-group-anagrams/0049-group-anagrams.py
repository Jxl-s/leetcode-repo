class Solution:
    def getStrKey(self, string):
        counts = [0] * 26
        for c in string:
            counts[ord(c) - ord('a')] += 1
        
        k = ''
        for i, c in enumerate(counts):
            if c > 0:
                k += str(c) + chr(ord('a') + i)
        
        return k

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = self.getStrKey(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        output = []
        for a in groups.values():
            output.append(a)
        
        return output