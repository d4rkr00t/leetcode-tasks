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
    sign = 1 if x >= 0 else -1
    x = abs(x)
    ans = 0

    while x:
        x, num = divmod(x, 10)
        ans = ans * 10 + num

        if ans > 2**31 - 1 or ans < -2**31:
            return 0

    return ans * sign


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
