# My Calendar II
# https://leetcode.com/problems/my-calendar-ii/
# medium
#
# Tags: Google
#
# Time:  O(c+b)
# Space: O(c+b)
#
# Solution:
# TBD


class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.conflicts = []

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.conflicts:
            if end > s1 and start < e1:
                return False

        for s1, e1 in self.bookings:
            if end > s1 and start < e1:
                self.conflicts.append((max(s1, start), min(e1, end)))

        self.bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true

# 1       5
#   2  3
