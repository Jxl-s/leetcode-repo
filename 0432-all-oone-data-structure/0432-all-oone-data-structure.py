class Node:
    def __init__(self, val=0):
        self.val = val
        self.strings = set()
        self.prev, self.next = None, None

    def add(self, word):
        self.strings.add(word)
    
    def remove(self, word):
        self.strings.remove(word)

    def is_empty(self):
        return len(self.strings) == 0

class DoublyList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        
        self.left.next = self.right
        self.right.prev = self.left

    def delete(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def add_after(self, node, new_node):
        prev, next = node, node.next
        prev.next, next.prev = new_node, new_node
        new_node.prev, new_node.next = prev, next

    def add_before(self, node, new_node):
        prev, next = node.prev, node
        prev.next, next.prev = new_node, new_node
        new_node.prev, new_node.next = prev, next

class AllOne:

    def __init__(self):
        self.list = DoublyList()
        self.map = {}

    def inc(self, key: str) -> None:
        node = self.list.left

        if key in self.map:
            node = self.map[key]
            node.remove(key)
        
        if node.next.val == node.val + 1:
            self.map[key] = node.next
            self.map[key].add(key)
        else:
            # create the new node
            new_node = Node(node.val + 1)
            new_node.add(key)

            self.map[key] = new_node
            self.list.add_after(node, new_node)
        
        if node.is_empty() and node.val > 0:
            self.list.delete(node)

    def dec(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.remove(key)
        
        if node.val - 1 == 0:
            if node.is_empty():
                self.list.delete(node)

            del self.map[key]
            return

        if node.prev.val == node.val - 1:
            self.map[key] = node.prev
            self.map[key].add(key)
        else:
            # create the new node
            new_node = Node(node.val - 1)
            new_node.add(key)

            self.map[key] = new_node
            self.list.add_before(node, new_node)
        
        if node.is_empty() and node.val > 0:
            self.list.delete(node)

    def getMaxKey(self) -> str:
        if self.list.right.prev == self.list.left:
            return ""
        
        return next(iter(self.list.right.prev.strings))

    def getMinKey(self) -> str:
        if self.list.left.next == self.list.right:
            return ""
        
        return next(iter(self.list.left.next.strings))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()