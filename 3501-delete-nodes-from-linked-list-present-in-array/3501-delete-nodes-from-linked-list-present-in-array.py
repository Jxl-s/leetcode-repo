# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        # find new head
        while head.val in nums:
            head = head.next
        
        current = head
        prev = None

        while current:
            if current.val in nums:
                prev.next = current.next
            else:
                prev = current

            current = current.next

        return head