# Plus One
# https://leetcode.com/problems/plus-one/
# easy
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def plusOne(digits: [int]) -> [int]:
    carry = 1

    for i in range(len(digits))[::-1]:
        cur = digits[i] + carry
        carry, digits[i] = divmod(cur, 10)

    if carry:
        digits.insert(0, carry)

    return digits

print(plusOne([1,2,3]), [1,2,4])
print(plusOne([4,3,2,1]), [4,3,2,2])
