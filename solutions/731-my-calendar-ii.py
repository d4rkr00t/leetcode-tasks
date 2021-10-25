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
        self.events = []
        self.doublebooked = []

    def book(self, start: int, end: int) -> bool:
        for s1, e1 in self.doublebooked:
            if s1 < end and e1 > start:
                return False

        for s1, e1 in self.events:
            if s1 < end and e1 > start:
                self.doublebooked.append((max(s1, start), min(e1, end)))

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

# |  |
#      |   |

# |  |
#   |   |

#    |  |
# |   |

#  |   |
#   | |
