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
    res = 0
    x = abs(x)

    while x:
        x, r = divmod(x, 10)
        res = res * 10 + r

    if res > 2**31-1:
        return 0

    return res * sign


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
print(reverse(1), 1)
print(reverse(0), 0)
