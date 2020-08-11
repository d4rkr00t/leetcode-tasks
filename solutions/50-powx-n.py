# Pow(x, n)
# https://leetcode.com/problems/powx-n/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n == 1:
        return x

    if n < 0:
        x = 1/x
        n = -n

    res = myPow(x, n // 2)
    res *= res

    if n % 2 == 1:
        res *= x

    return res


print(myPow(2.00000, 10), 1024.00000)
print(myPow(2.10000, 3), 9.26100)
print(myPow(2.00000, -2), 0.25000)
