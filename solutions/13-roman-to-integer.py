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
    ans = 0
    pos = 0
    while pos < len(s):
        ch = s[pos]
        if pos + 1 < len(s) and table[s[
                pos + 1]] > table[ch] and ch + s[pos + 1] in table:
            ch += s[pos + 1]
            ans += table[ch]
            pos += 2
        else:
            ans += table[ch]
            pos += 1

    return ans


print(romanToInt("III"), 3)
print(romanToInt("IV"), 4)
print(romanToInt("IX"), 9)
print(romanToInt("LVIII"), 58)
print(romanToInt("MCMXCIV"), 1994)
