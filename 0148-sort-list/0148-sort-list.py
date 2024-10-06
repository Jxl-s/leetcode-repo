# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        cur = head

        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        nums.sort()
        cur = head
        i = 0

        while cur:
            cur.val = nums[i]
            cur = cur.next
            i += 1
        
        return head