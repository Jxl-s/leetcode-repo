# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find length
        length, cur = 0, head
        while cur:
            length += 1
            cur = cur.next

        # Find start of second part
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start = slow
        if length % 2 == 1:
            start = slow.next
        
        # Reverse second part
        prev = None
        cur = start
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Two pointers
        i = head
        j = prev

        while i and j:
            if i.val != j.val:
                return False

            i = i.next
            j = j.next

        return True