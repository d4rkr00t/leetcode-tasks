# Min Stack
# https://leetcode.com/problems/min-stack/
# easy
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")

    def push(self, x: int) -> None:
        self.stack.append((x, self.min))
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        _, m = self.stack.pop()
        self.min = m

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
