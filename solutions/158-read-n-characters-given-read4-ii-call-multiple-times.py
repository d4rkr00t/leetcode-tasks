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

# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

import math

class Solution:
    def __init__():
        self.carry = []

    def __read_from_carry__(self, buf, n) -> int:
        n = min(n, len(self.carry))
        for i in range(n):
            buf[i] = self.carry[i]

        self.carry = self.carry[n:]
        return n

    def __write_to_carry__(self, n):
        nn = math.ceil(n/4)
        temp = []

        for _ in range(nn):
            buf = [None] * 4
            num = read4(buf)
            temp.extend(num[:num])

        self.carry.extend(temp)


    def read(self, buf: List[str], n: int) -> int:
        if len(self.carry) - 1 >= n:
            return self.__read_from_carry__(buf, n)

        self.__write_to_carry__(n - len(self.carry))
        return self.__read_from_carry__(n)

