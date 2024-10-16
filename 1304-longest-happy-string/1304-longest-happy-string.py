class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0: heap.append((-a, 'a'))
        if b > 0: heap.append((-b, 'b'))
        if c > 0: heap.append((-c, 'c'))

        heapq.heapify(heap)
        count = 1
        prev = ''

        output = ""
        while len(heap) > 0:
            total, char = heapq.heappop(heap)
            total = -total

            # Try next char if current is bad
            if char == prev and count == 3:
                # get the next char
                count = 1
                if len(heap) == 0:
                    return output

                next_total, next_char = heapq.heappop(heap)
                next_total = -next_total

                prev = next_char
                next_total -= 1
                output += next_char

                if next_total > 0:
                    heapq.heappush(heap, (-next_total, next_char))
                
                heapq.heappush(heap, (-total, char))
            else:
                count += 1
                total -= 1
                output += char
                prev = char

                if total > 0:
                    heapq.heappush(heap, (-total, char))

        return output