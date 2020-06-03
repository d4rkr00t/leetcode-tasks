# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Math

def reverse(x: int) -> int:
    sign = -1 if x != abs(x) else 1
    x = abs(x)
    ans = 0

    while x > 0:
        x,n = divmod(x, 10)
        ans = ans * 10 + n


    return ans * sign if ans <= 2**31 else 0

print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
