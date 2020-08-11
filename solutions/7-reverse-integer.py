# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0

    while x:
        x, d = divmod(x, 10)
        res = res * 10 + d

    if sign * res > 2**31 - 1 or sign * res < -(2**31):
        return 0

    return sign * res


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
