# Read N Characters Given Read4 II - Call multiple times
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
# hard
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def read4(buf4: List[str]) -> int:
    pass


class Solution:
    buf = []
    offset = 0

    def read(self, buf: List[str], n: int) -> int:
        while n > len(self.buf) - self.offset:
            temp_buf = [None] * 4
            count = read4(temp_buf)
            if count == 0:
                break

            for i in range(count):
                self.buf.append(temp_buf[i])

        diff = n - (len(self.buf) - self.offset)
        if diff > 0:
            self.__writeBuf__(n - diff, buf)
            return n - diff

        self.__writeBuf__(n, buf)
        return n

    def __writeBuf__(self, n, buf):
        for i in range(n):
            buf[i] = self.buf[self.offset + i]

        self.offset += n


# file = "abc", queries = [1,2,1]
# self.buf = ["a", "b", "c"]
# self.offset = 3
#
# q1 - ["a"] 1
# q2 – ["b", "c"] 2
# q3 – [] 0
