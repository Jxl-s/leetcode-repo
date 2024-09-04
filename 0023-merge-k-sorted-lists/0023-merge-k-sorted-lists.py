# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode()
            head = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                
                head = head.next

            head.next = l1 if l1 else l2
            return dummy.next
        
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(merge(l1, l2))
    
        return lists[0] if lists else None