# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# hard
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -self.lo[0])
        heapq.heappop(self.lo)

        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]

        return ((-self.lo[0]) + self.hi[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 2 1 4 5 8 3

# min_q: 2 3
# max_q: 1
