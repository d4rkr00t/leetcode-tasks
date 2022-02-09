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
        self.min = None

    def push(self, x: int) -> None:
        self.stack.push((x, self.min))
        self.min = min(x, self.min)

    def pop(self) -> None:
        _, prev_min = self.stack.pop()
        self.min = prev_min

    def top(self) -> int:
        self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
