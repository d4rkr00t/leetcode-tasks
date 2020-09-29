# String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# medium
#
# Tags: Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def myAtoi(str: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)
    num = 0
    sign = 1
    seen_num = False

    for ch in str:
        if seen_num and not ch.isdigit():
            break

        if ch == "+" or ch == "-":
            seen_num = True
            sign = -1 if ch == "-" else 1

        elif ch.isdigit():
            seen_num = True
            num = (num * 10) + int(ch)
        elif ch == " ":
            continue
        else:
            return 0

    result = num * sign

    if result > INT_MAX:
        return INT_MAX

    if result < INT_MIN:
        return INT_MIN

    return result


print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)
