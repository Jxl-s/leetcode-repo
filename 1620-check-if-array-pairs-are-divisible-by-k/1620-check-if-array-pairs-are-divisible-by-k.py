class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = defaultdict(int)

        for n in arr:
            mod = ((n % k) + k) % k
            complement = (k - mod) % k

            if rem[complement] == 0:
                rem[mod] += 1
            else:
                rem[complement] -= 1

        return all(count == 0 for count in rem.values())