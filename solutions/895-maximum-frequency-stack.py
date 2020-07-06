# Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# hard
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


class FreqStack:

    def __init__(self):
        self.group = collections.defaultdict(list)
        self.count = collections.Counter()
        self.max = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.group[self.count[x]].append(x)
        self.max = max(self.count[x], self.max)

    def pop(self) -> int:
        top = self.group[self.max].pop()
        self.count[top] -= 1

        if not self.group[self.max]:
            self.max -= 1

        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
