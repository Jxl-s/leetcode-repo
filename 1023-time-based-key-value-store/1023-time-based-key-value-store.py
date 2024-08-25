class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        arr = self.map[key]
        if timestamp < arr[0][0]:
            return ""

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]

            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        # when right is under left, we take under
        return arr[right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)