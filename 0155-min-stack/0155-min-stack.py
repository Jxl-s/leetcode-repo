class MinStack:
    def __init__(self):
        self.s1 = []

        # use a separate stack to store current minimums
        # might be filled like (1, 1, 1, 0, 0, -2, -2, -3, ...) will just get smaller
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if len(self.s2) == 0:
            self.s2.append(val)
        else:
            self.s2.append(min(val, self.s2[-1]))

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()