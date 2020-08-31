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
from math import ceil


def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self.overflow = []

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        read = 0
        while n:
            if not self.overflow:
                tmp_buf = [None] * 4
                res = read4(tmp_buf)
                if not res:
                    return read

                tmp_buf = tmp_buf[:res][::-1]
                self.overflow = tmp_buf

            if self.overflow:
                buf[i] = self.overflow.pop()
                i += 1
                read += 1

        return read
