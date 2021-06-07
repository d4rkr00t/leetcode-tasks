# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(log(N))
# Space: O(1)
#
# Solution:
# TBD


def reverse(x: int) -> int:
    max_int = 2**31 - 1
    min_int = -2**31
    sign = -1 if x < 0 else 1
    x = abs(x)
    ans = 0

    while x:
        x, d = divmod(x, 10)
        ans = ans * 10 + d

    ans = ans * sign
    if ans > max_int or ans < min_int:
        return 0

    return ans


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
