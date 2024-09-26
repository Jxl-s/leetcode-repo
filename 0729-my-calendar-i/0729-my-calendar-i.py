class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left, self.right = None, None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        self.root, can_book = self._insert(self.root, start, end)
        return can_book

    def _insert(self, parent, start, end):
        if not parent:
            return (TreeNode(start, end), True)

        if start < parent.end and end > parent.start:
            return (parent, False)

        can_book = True
        if start >= parent.end:
            parent.right, can_book = self._insert(parent.right, start, end)
        else:
            parent.left, can_book = self._insert(parent.left, start, end)

        return (parent, can_book)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)