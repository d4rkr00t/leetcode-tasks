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
    table = {
        0: "",
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

    ans = ""
    for nn in [1000, 100, 10]:
        cur, num = divmod(num, nn)
        if cur * nn in table:
            ans += table[cur * nn]
        else:
            ans += table[nn] * cur

    res = []
    while num not in table:
        res.append(table[1])
        num -= 1

    res.append(table[num])
    ans += "".join(res[::-1])

    return ans


print(intToRoman(3), "III")
print(intToRoman(4), "IV")
print(intToRoman(9), "IX")
print(intToRoman(58), "LVIII")
print(intToRoman(1994), "MCMXCIV")
