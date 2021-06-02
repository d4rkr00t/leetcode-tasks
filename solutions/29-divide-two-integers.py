# Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(log(n) * log(n))
# Space: O(1)
#
# Solution:
# Exponential substraction


def divide(dividend: int, divisor: int) -> int:
    max_int = 2**31 - 1
    min_int = -2**31
    if divisor == 0:
        return None

    ans = 0
    sign = (-1 if dividend < 0 else 1) * (-1 if divisor < 0 else 1)

    divisor = abs(divisor)
    dividend = abs(dividend)

    while dividend >= divisor:
        powerOfTwo = 1
        value = divisor

        while value + value < dividend:
            value += value
            powerOfTwo += powerOfTwo

        dividend -= value
        ans += powerOfTwo

    ans = ans * sign
    if ans < min_int:
        return min_int

    if ans > max_int:
        return max_int

    return ans


print(divide(dividend=10, divisor=3), 3)
print(divide(dividend=7, divisor=-3), -2)
print(divide(dividend=-1, divisor=1), -2)
