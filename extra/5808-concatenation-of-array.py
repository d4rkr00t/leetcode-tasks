# https://leetcode.com/contest/weekly-contest-249/problems/concatenation-of-array/

from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums


print(getConcatenation([1, 3, 2, 1]))
