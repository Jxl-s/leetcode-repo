# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge(head1, head2):
            dummy = ListNode()
            head = dummy

            while head1 or head2:
                next_node = None
                if head1 and head2:
                    next_node = head1 if head1.val < head2.val else head2
                else:
                    next_node = head1 if head1 else head2

                head.next = next_node
                head = head.next

                if next_node == head1:
                    head1 = head1.next
                
                if next_node == head2:
                    head2 = head2.next

            return dummy.next

        current = lists[0]
        for i in range(1, len(lists)):
            current = merge(current, lists[i])

        return current