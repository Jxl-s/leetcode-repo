class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        if timestamp < arr[0][0]: # timestamp less than first element, early return
            return ""

        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right + 1) // 2

            if arr[mid][0] == timestamp:
                left = mid
                break

            if arr[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        return arr[left][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)