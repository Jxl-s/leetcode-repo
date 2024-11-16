class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Store longest increasing subsequence
        prefix = [0] * n

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix[i] = prefix[i - 1] + 1

        results = [-1] * (n - k + 1)
        for j in range(k - 1, n):
            i = j - k + 1

            # Check if the sequence is ongoing
            if prefix[i] + k - 1 == prefix[j]:
                results[i] = nums[j]

        return results