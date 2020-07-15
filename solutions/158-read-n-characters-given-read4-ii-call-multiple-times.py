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

import math


def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self.ibuff = []
        self.pointer = 0
        self.reached_end = False

    def read_from_file(self, n):
        if self.reached_end:
            return

        number_of_reads = math.ceil(
            (n - (len(self.ibuff) - self.pointer - 1)) / 4)

        for i in range(number_of_reads):
            buf = [""] * 4
            res = read4(buf)
            self.ibuff += [b for b in buf if b]

            if res < 4:
                self.reached_end = True
                break

    def read(self, buf: List[str], n: int) -> int:
        if n > len(self.ibuff) - self.pointer - 1:
            self.read_from_file(n)

        read_data = 0
        for i in range(self.pointer, min(self.pointer + n, len(self.ibuff))):
            buf[read_data] = self.ibuff[i]
            self.pointer += 1
            read_data += 1

        return read_data
