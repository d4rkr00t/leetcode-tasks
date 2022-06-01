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
    num = 0
    sign = 1
    seenNumber = False
    maxInt = 2**31 - 1
    minInt = -2**31

    for ch in str:
        if ch.isdigit():
            num = num * 10 + int(ch)
            seenNumber = True
        elif seenNumber:
            break
        elif ch == " ":
            continue
        elif ch == "-" or ch == "+":
            sign = -1 if ch == "-" else 1
            seenNumber = True
        else:
            break

    return max(min(num * sign, maxInt), minInt)


print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)
