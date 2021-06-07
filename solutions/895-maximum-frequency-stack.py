# Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# hard
#
# Tags: Amazon
#
# Time:  push = O(log(n)), pop = O(log(n))
# Space: O(n)
#
# Solution:
# TBD

import heapq


class FreqStack:
    def __init__(self):
        self.hq = []
        self.freq = {}
        self.counter = 0

    def push(self, x: int) -> None:
        self.freq[x] = self.freq.get(x, 0)
        self.freq[x] += 1
        heapq.heappush(self.hq, (-self.freq[x], -self.counter, x))
        self.counter += 1

    def pop(self) -> int:
        (_, _, x) = heapq.heappop(self.hq)
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
