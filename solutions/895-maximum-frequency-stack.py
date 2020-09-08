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

import heapq
import collections


class FreqStack:

    def __init__(self):
        self.hq = []
        self.freq = collections.Counter()

    def push(self, x: int) -> None:
        self.freq[x] += 1
        heapq.heappush(self.hq, (self.freq[x], x))

    def pop(self) -> int:
        _, x = heapq.heapop(self.hq)
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
