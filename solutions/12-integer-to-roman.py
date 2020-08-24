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
    n_to_r = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    ans = ""

    for n in [1000, 100, 10, 1]:
        div = num // n
        if div == 0:
            continue

        num -= div * n
        ir = ""
        while div:
            if div * n in n_to_r:
                ir = n_to_r[div * n] + ir
                break
            else:
                ir = n_to_r[n] + ir

            div -= 1
        ans += ir

    return ans


print(intToRoman(3), "III")
print(intToRoman(4), "IV")
print(intToRoman(9), "IX")
print(intToRoman(58), "LVIII")
print(intToRoman(60), "LX")
print(intToRoman(68), "LXVIII")
print(intToRoman(168), "CLXVIII")
print(intToRoman(1994), "MCMXCIV")
