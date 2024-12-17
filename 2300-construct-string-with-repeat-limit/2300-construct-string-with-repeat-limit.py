class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(x), c) for x, c in Counter(s).items()]
        heapq.heapify(heap)

        output = ''
        previous = None

        while heap:
            char, real_count = heapq.heappop(heap)
            count = real_count

            if previous:
                heapq.heappush(heap, previous)
                if -previous[0] > -char:
                    count = 1

                previous = None

            use_count = min(repeatLimit, count)
            output += chr(-char) * use_count

            real_count -= use_count
            if real_count <= 0:
                continue

            previous = (char, real_count)

        return output