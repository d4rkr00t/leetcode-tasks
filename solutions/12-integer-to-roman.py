# Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
# medium
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def intToRoman(num: int) -> str:
    table = {1: "I",
             4: "IV",
             5: "V",
             9: "IX",
             10: "X",
             40: "XL",
             50: "L",
             90: "XC",
             100: "C",
             400: "CD",
             500: "D",
             900: "CM",
             1000: "M",
             }

    def convert(ans, num, p):
        if num == 0:
            return ans

        cur = (num % 10) * (10**p)
        num = num // 10

        while cur > 0:
            if cur in table:
                ans = table[cur] + ans
                break

            dec = 10**p
            ans = table[dec] + ans
            cur -= dec

        return convert(ans, num, p+1)

    return convert("", num, 0)


print(intToRoman(3), "III")
print(intToRoman(4), "IV")
print(intToRoman(9), "IX")
print(intToRoman(58), "LVIII")
print(intToRoman(1994), "MCMXCIV")
