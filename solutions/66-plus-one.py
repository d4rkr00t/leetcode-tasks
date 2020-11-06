# Plus One
# https://leetcode.com/problems/plus-one/
# easy
#
# Tags: Google
#
# Time:  O(n)
# Space: O(1)

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    carry = 1
    pos = len(digits) - 1

    while pos >= 0 and carry:
        carry, digits[pos] = divmod(digits[pos]+carry, 10)
        pos -= 1

    if carry:
        digits.appendleft(carry)

    return digits


print(plusOne([1, 2, 3]), [1, 2, 4])
print(plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
