# Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def divide(dividend: int, divisor: int) -> int:
    sign = -1 if divisor < 0 else 1
    if dividend < 0:
        sign = sign * -1

    divisor = abs(divisor)
    dividend = abs(dividend)

    if dividend < divisor:
        return 0

    min_int = -(2**31)
    max_int = 2**31 - 1
    cur = divisor
    count = 1

    while True:
        if cur + cur > dividend:
            ans = count + divide(dividend - cur, divisor)
            ans = -ans if sign < 0 else ans

            if ans > max_int:
                return max_int
            elif ans < min_int:
                return min_int
            return ans

        count += count
        cur += cur


print(divide(dividend=10, divisor=3), 3)
print(divide(dividend=7, divisor=-3), -2)

# 26 / 3
# (((3 + 3) + 6) + 12) = 24
# 2 / 3
