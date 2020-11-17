# Min Stack
# https://leetcode.com/problems/min-stack/
# easy
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(1)
# Space: O(N)
#
# Solution:
# Two stacks

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_values = []

    def push(self, x: int) -> None:
        if x <= self.getMin():
            self.min_values.append(x)

        self.stack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.getMin():
            self.min_values.pop()

        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_values:
            return self.min_values[-1]

        return float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
