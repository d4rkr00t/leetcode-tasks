# Maximum Number of Weeks for Which You Can Work
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
# medium

from typing import List


def numberOfWeeks(milestones: List[int]) -> int:
    _sum, _max = sum(milestones), max(milestones)
    if _sum - _max >= _max:
        return _sum
    return 2 * (_sum - _max) + 1


print(numberOfWeeks([1, 2, 3]), 6)
print(numberOfWeeks([5, 2, 1]), 7)
print(numberOfWeeks([5, 2, 1, 10, 8]), 26)
