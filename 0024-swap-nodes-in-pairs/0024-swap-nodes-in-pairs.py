# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        cur = head
        original = head.next

        while cur and cur.next:
            if prev:
                prev.next = cur.next
            
            temp = cur.next.next
            cur.next.next = cur
            cur.next = temp

            prev = cur
            cur = temp

        return original