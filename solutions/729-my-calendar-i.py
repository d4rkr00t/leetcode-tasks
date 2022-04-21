# My Calendar I
# https://leetcode.com/problems/my-calendar-i/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class Node:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if self.start < node.end and self.end > node.start:
            return False

        if node.end <= self.start:
            if self.left:
                return self.left.insert(node)
            self.left = node
        else:
            if self.right:
                return self.right.insert(node)
            self.right = node


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        if not self.root:
            self.root = node
            return True

        return self.root.insert(node)


#   [10,20]
#   /    \
# [9,10]  [20, 21]
