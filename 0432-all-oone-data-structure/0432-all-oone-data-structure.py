class Node:
    def __init__(self, val=0):
        self.val = val
        self.next, self.prev = None, None
        self.words = set()

    def add_word(self, word):
        self.words.add(word)
    
    def remove_word(self, word):
        self.words.remove(word)

    def is_empty(self):
        return len(self.words) == 0
    
    def destroy(self):
        prev, next = self.prev, self.next
        if prev and next:
            prev.next, next.prev = next, prev

        self.prev, self.next = None, None

class AllOne:
    def __init__(self):
        self.counter = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def inc(self, key: str) -> None:
        node = self.left

        if key in self.counter:
            node = self.counter[key]
            node.remove_word(key)

        # Switching node for the word
        # if the next node exists, add it to it
        if node.next.val == node.val + 1:
            self.counter[key] = node.next
            node.next.add_word(key)
        else:
            # else we create the new node
            prev, next = node, node.next
            new_node = Node(node.val + 1)
            new_node.prev, new_node.next = prev, next
            prev.next, next.prev = new_node, new_node

            new_node.add_word(key)
            self.counter[key] = new_node

        if node.is_empty() and node != self.left:  
            node.destroy()


    def dec(self, key: str) -> None:
        node = self.right

        if key in self.counter:
            node = self.counter[key]
            node.remove_word(key)

        # Switching node for the word
        # if the next node exists, add it to it
        if node.prev.val == node.val - 1:
            self.counter[key] = node.prev
            node.prev.add_word(key)
        else:
            # else we create the new node
            prev, next = node.prev, node
            new_node = Node(node.val - 1)
            new_node.prev, new_node.next = prev, next
            prev.next, next.prev = new_node, new_node

            new_node.add_word(key)
            self.counter[key] = new_node

        if node.is_empty() and node != self.right:
            node.destroy()

    def getMaxKey(self) -> str:
        if self.right.prev == self.left:
            return ""

        return next(iter(self.right.prev.words))

    def getMinKey(self) -> str:
        if self.left.next == self.right:
            return ""

        return next(iter(self.left.next.words))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()