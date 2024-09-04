# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            while l:
                heap.append(l.val)
                l = l.next

        heapq.heapify(heap)
        dummy = ListNode()
        head = dummy

        while len(heap) > 0:
            node = ListNode(heapq.heappop(heap))
            head.next = node
            head = head.next
        
        return dummy.next