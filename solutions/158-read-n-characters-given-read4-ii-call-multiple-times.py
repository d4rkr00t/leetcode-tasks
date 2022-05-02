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

from collections import deque
import math
from typing import List


def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self) -> None:
        self.carry = deque()
        self.eof = False

    def __readIntoTmpBuf(self, n):
        if self.eof:
            return

        needToRead = math.ceil((n - len(self.carry)) / 4)

        for _ in range(needToRead):
            tmpBuf = [0] * 4
            tmpRes = read4(tmpBuf)

            for i in range(tmpRes):
                self.carry.append(tmpBuf[i])

            if tmpRes < 4:
                self.eof = True
                break

    def read(self, buf: List[str], n: int) -> int:
        if len(self.carry) < n:
            self.__readIntoTmpBuf(n)

        i = 0
        unread = n
        while unread and self.carry:
            buf[i] = self.carry.popleft()
            unread -= 1
            i += 1

        return n - unread
