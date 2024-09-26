class TreeNode:
    def __init__(self,val=None):
        self.value = val

        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        self.root, can_book = self._insert(self.root, start, end)
        return can_book

    def _insert(self, parent, start, end):
        if not parent:
            return (TreeNode((start, end)), True)

        if start < parent.value[1] and end > parent.value[0]:
            return (parent, False)

        can_book = True
        if start >= parent.value[1]:
            parent.right, can_book = self._insert(parent.right, start, end)
        else:
            parent.left, can_book = self._insert(parent.left, start, end)

        return (parent, can_book)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)