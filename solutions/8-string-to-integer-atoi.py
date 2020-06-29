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

def myAtoi(str) -> int:
    def consume_char(str, pos, res, sign, seenNumber):
        if pos == len(str):
            ans = int(res) if res else 0
            if ans >= 2**31:
                ans = 2**31 if sign and sign < 0 else 2**31-1

            return ans * (sign or 1)

        char = str[pos]

        if char.isdigit():
            return consume_char(str, pos + 1, res + char, sign, True)

        if not char.isdigit() and seenNumber:
            return consume_char(str, len(str), res, sign, seenNumber)

        if char == "+" or char == "-":
            if sign or seenNumber: return 0
            sign = -1 if char == "-" else 1
            return consume_char(str, pos + 1, res, sign, True)

        elif not char.isdigit() and char != " ":
            return 0

        return consume_char(str, pos + 1, res, sign, seenNumber)


    return consume_char(str, 0, "", None, False)

print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("-91283472332"), -2147483648)

