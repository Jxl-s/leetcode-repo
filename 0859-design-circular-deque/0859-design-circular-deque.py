class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev, self.next = None, None

class MyCircularDeque:
    def __init__(self, k: int):
       self.max_size = k
       self.size = 0

       self.left = Node()
       self.right = Node()

       self.left.next = self.right
       self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        prev, next = self.left, self.left.next

        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        prev, next = self.right.prev, self.right

        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        node = self.left.next
        prev, next = node.prev, node.next

        prev.next, next.prev = next, prev
        node.prev, node.next = None, None

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        node = self.right.prev
        prev, next = node.prev, node.next

        prev.next, next.prev = next, prev
        node.prev, node.next = None, None

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()