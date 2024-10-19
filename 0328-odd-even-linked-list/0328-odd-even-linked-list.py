# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_evens = ListNode()
        dummy_odds = ListNode()

        evens = dummy_evens
        odds = dummy_odds

        i = 1
        while head:
            if i % 2 == 0:
                evens.next = head
                evens = evens.next
            else:
                odds.next = head
                odds = odds.next

            i += 1
            head = head.next

        evens.next = None
        odds.next = dummy_evens.next

        return dummy_odds.next