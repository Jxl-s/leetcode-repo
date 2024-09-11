# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        before = None
        prev = head
        cur = prev.next
        original = cur

        while cur:
            if before:
                before.next = cur
            
            temp = cur.next
            cur.next = prev
            prev.next = temp
            before = prev
            prev = temp
            if temp and temp.next:
                cur = temp.next
            else:
                cur = None
        
        return original