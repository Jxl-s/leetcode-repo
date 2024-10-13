class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_num = nums[0][0]

        for i in range(len(nums)):
            heap.append((nums[i][0], i, 0)) # start pointer at index 0
            max_num = max(max_num, nums[i][0])
        
        heapq.heapify(heap)
        output = [heap[0][0], max_num]

        while len(heap) > 0:
            # Finds the row with smallest current pointer
            item, i, j = heapq.heappop(heap)
            if j >= len(nums[i]) - 1:
                return output

            # Slide to the next j
            next_num = nums[i][j + 1]
            heapq.heappush(heap, (next_num, i, j + 1))
            
            max_num = max(max_num, next_num)

            # check if the range is smaller
            cur_dist = max_num - heap[0][0]
            out_dist = output[1] - output[0]
            if cur_dist < out_dist:
                output[0] = heap[0][0]
                output[1] = max_num

        return output