# Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# hard
#
# Tags: Amazon
#
# Time:  O(log(n)) – insert, O(log(n)) – pop
# Space: O(n)
#
# Solution:
# TBD

import heapq


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.order = 0
        self.hq = []

    def push(self, x: int) -> None:
        freq = self.freq.get(x, 0) + 1
        self.freq[x] = freq
        heapq.heappush(self.hq, (-freq, -self.order, x))
        self.order += 1

    def pop(self) -> int:
        (_, _, x) = heapq.heappop(self.hq)
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
