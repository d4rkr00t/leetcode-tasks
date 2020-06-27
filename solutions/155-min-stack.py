# Min Stack
# https://leetcode.com/problems/min-stack/
# easy
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: O(n)
#
# Solution:
# TBD

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        smallest = min(float("inf") if not self.stack else self.stack[-1][1], x)
        self.stack.append((x, smallest))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
