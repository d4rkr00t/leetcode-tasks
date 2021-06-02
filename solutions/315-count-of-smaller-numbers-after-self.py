# Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# hard
#
# Tags: Google, Amazon, Microsoft
#
# Time:  O(n*log(n))
# Space: O(n)
#
# Solution:
# Merge Sort

from typing import List


def countSmaller(nums: List[int]) -> List[int]:
    smaller = [0] * len(nums)

    def sort(enum):
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    sort(list(enumerate(nums)))

    return smaller


print(countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])

# [5, 2 ,6, 1]
# [1, 2, 5, 6]
#  ^
#
