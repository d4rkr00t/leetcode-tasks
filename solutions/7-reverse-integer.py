# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD


def reverse(x: int) -> int:
    ans = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)

    while x:
        x, n = divmod(x, 10)
        ans = ans * 10 + n

    ans = ans * sign

    if ans > 2**31 - 1 or ans < -2**31:
        return 0

    return ans


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
