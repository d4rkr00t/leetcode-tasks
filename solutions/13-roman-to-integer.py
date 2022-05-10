# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def romanToInt(s: str) -> int:
    table = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    prev = ""
    ans = 0
    for ch in s[::-1]:
        if not prev:
            prev = ch
            continue

        if ch + prev in table:
            ans += table[ch + prev]
            prev = ""
        else:
            ans += table[prev]
            prev = ch

    if prev:
        ans += table[prev]

    return ans


print(romanToInt("III"), 3)
print(romanToInt("IV"), 4)
print(romanToInt("IX"), 9)
print(romanToInt("LVIII"), 58)
print(romanToInt("MCMXCIV"), 1994)
