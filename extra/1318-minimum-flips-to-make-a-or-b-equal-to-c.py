# Minimum Flips to Make a OR b Equal to c
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# medium
#
# Tags: Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def minFlips(a: int, b: int, c: int) -> int:
    ans = 0

    if a | b == c:
        return ans

    while a or b or c:
        a_b = a & 1
        b_b = b & 1
        c_b = c & 1

        if a_b | b_b != c_b:
            if c_b:
                ans += 1
            else:
                ans += a_b + b_b

        a, b, c = a >> 1, b >> 1, c >> 1

    return ans


print(minFlips(a=2, b=6, c=5), 3)
print(minFlips(a=4, b=2, c=7), 1)
print(minFlips(a=1, b=2, c=3), 0)
