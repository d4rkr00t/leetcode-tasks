# My Calendar II
# https://leetcode.com/problems/my-calendar-ii/
# medium
#
# Tags: Google
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# Brute Force

class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []


    def book(self, start: int, end: int) -> bool:
        evt = (start, end)

        for x,y in self.overlaps:
            if start < y and end > x:
                return False

        for x,y in self.events:
            if start < y and end > x:
                self.overlaps.append(((max(start, x), min(end, y))))

        self.events.append(evt)
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true

(5, 15) (10, 20) (10, 40) (50,60)

# ----
#    --
