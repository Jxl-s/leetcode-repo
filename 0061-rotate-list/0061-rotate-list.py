# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Get the length of the list
        list_len = 0
        cur = head
        last_node = None

        while cur:
            list_len += 1
            cur = cur.next
            if cur:
                last_node = cur
        
        k %= list_len
        if k == 0:
            return head
        
        i = 0
        cur = head
        for _ in range(list_len - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        last_node.next = head
        return new_head