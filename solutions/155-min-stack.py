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
        self.min_stack = []

    def push(self, x: int) -> None:
        m = self.min_stack[-1] if self.min_stack else (float("inf"), 1)

        if x < m[0]:
            self.min_stack.append((x, 0))

        if x == self.min_stack[-1][0]:
            self.min_stack[-1] = (x, self.min_stack[-1][1] + 1)

        self.stack.append(x)

    def pop(self) -> None:
        item = self.stack.pop()

        if item == self.min_stack[-1]:
            if self.min_stack[-1][1] - 1 == 0:
                self.min_stack.pop()
            else:
                self.min_stack[-1] = (item, self.min_stack[-1][1] - 1)

        return item

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1][0] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
