# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None for i in range(k)]

        if k == 1:
            return [head]

        total_len = 0
        temp = head

        while temp:
            total_len += 1
            temp = temp.next
        
        chunk_size = total_len // k
        remainder = total_len % k
        
        output = []
        for _ in range(k):
            # find nodes in group
            part_size = chunk_size + (1 if remainder > 0 else 0)
            remainder -= 1

            if not head:
                output.append(None)
            else:
                start_node = head
                output.append(head)

                for _ in range(1, part_size):
                    if head:
                        head = head.next

                if head:
                    temp = head.next
                    head.next = None
                    head = temp

        return output