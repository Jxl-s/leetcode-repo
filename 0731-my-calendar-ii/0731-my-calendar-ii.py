class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.nice_bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if end > s and e > start:
                return False

        for s, e in self.nice_bookings:
            if end > s and e > start:
                self.bookings.append((max(s, start), min(e, end)))

        self.nice_bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)