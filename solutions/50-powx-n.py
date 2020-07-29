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
    def fastPower(x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n

        half = fastPower(x, n//2)
        if n % 2 == 0:
            return half * half

        return half * half * x

    return fastPower(x, n)


print(myPow(2.00000, 10), 1024.00000)
print(myPow(2.10000, 3), 9.26100)
print(myPow(2.00000, -2), 0.25000)
print(myPow(-2.00000, -2), 0.25000)
