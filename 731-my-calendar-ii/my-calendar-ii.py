from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.events = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        self.events.add((start, 1))
        self.events.add((end, -1))
        total = 0

        for i, j in self.events:
            total += j
            if total == 3:
                self.events.remove((start, 1))
                self.events.remove((end, -1))
                return False
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)