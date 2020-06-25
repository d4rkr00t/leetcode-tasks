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

class FreqStack:

    def __init__(self):
        self.pq = []
        self.elems = {}

    def push(self, x: int) -> None:
        self.elems[x] = self.elems.get(x, 0) + 1
        heapq.heappush(self.pq, (-self.elems[x], x))

    def pop(self) -> int:
        if not self.pq:
            return -1

        freq, item = heapq.heappop(self.pq)
        self.elems[item] -= 1

        return item

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
