class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        selection = random.randint(0, self.total - 1)
        current = 0

        for i in range(len(self.weights)):
            current += self.weights[i]
            if current > selection:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()