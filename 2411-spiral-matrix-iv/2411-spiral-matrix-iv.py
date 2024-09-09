# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        output = [[-1] * n for _ in range(m)]

        if n == 1:
            i = 0
            while head:
                output[i][0] = head.val
                head = head.next
                i += 1
            
            return output

        i, j = 0, 0

        wall_top = 0
        wall_right = n
        wall_bottom = m
        wall_left = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        while head:
            output[i][j] = head.val
            di, dj = directions[direction]

            i += di
            j += dj

            if direction == 0 and j + 1 == wall_right:
                wall_right -= 1
                direction = 1
            elif direction == 1 and i + 1 == wall_bottom:
                wall_bottom -= 1
                direction = 2
            elif direction == 2 and j - 1 == wall_left:
                wall_left += 1
                direction = 3
            elif direction == 3 and i - 1 == wall_top:
                wall_top += 1
                direction = 0

            head = head.next

        return output