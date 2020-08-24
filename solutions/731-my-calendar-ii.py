# My Calendar II
# https://leetcode.com/problems/my-calendar-ii/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if end > s and start < e:
                return False

        for s, e in self.events:
            if end > s and start < e:
                self.overlaps.append((max(s, start), min(e, end)))

        self.events.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
