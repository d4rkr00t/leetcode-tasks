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
    i_to_r = {
        1: "I",
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

    def recur(ans, num, p):
        if num == 0:
            return ans

        cur = (num % 10) * (10**p)
        num = num // 10

        while cur > 0:
            if cur in i_to_r:
                ans = i_to_r[cur] + ans
                break

            dec = 10 ** p
            ans = i_to_r[dec] + ans
            cur -= dec

        return recur(ans, num, p+1)

    return recur("", num, 0)

print(intToRoman(3), "III")
print(intToRoman(4), "IV")
print(intToRoman(9), "IX")
print(intToRoman(58), "LVIII")
print(intToRoman(1994), "MCMXCIV")
