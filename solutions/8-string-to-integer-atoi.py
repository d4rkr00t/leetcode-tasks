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
    sign = 1
    seenNum = False
    ans = 0
    min_int = -(2**31)
    max_int = 2**31 - 1

    for ch in str:
        if not ch.isnumeric() and seenNum:
            break

        if ch == "-":
            sign = -1
            seenNum = True
        elif ch == "+":
            sign = 1
            seenNum = True
        elif ch.isnumeric():
            ans = ans * 10 + int(ch)
            seenNum = True
        elif ch == " ":
            pass
        else:
            break

    ans = ans * sign

    if ans > max_int:
        return max_int

    return max(min_int, ans)


print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)
