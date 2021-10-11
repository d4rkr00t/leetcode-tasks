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

    for n in [1000, 100, 10]:
        cur, num = divmod(num, n)
        cur = cur * n
        if cur in table:
            ans += table[cur]
        else:
            temp = ""
            while cur:
                if cur in table:
                    temp += table[cur]
                    break
                else:
                    temp += table[n]
                    cur -= n

            ans += temp[::-1]

    if num > 0:
        ans += table[num]

    return ans


print(intToRoman(3), "III")
print(intToRoman(4), "IV")
print(intToRoman(9), "IX")
print(intToRoman(58), "LVIII")
print(intToRoman(80), "LXXX")
print(intToRoman(1994), "MCMXCIV")
