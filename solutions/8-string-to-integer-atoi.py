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

def myAtoi(s: str) -> int:
    acc = ""
    sign = None

    for c in s:
        if c.isdigit():
            acc += c
            continue
        if c == "-" or c == "+":
            if acc or sign:
                acc = ""
                break
            else:
                sign = 1 if c == "+" else -1
        elif c == " ":
            continue
        else:
            break

    if acc:
        res = int(acc) * (sign if sign else 1)
        if res > 2**31:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res

    return 0



print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)

