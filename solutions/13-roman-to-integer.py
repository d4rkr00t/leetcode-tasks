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
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ans = 0

    for i, c in enumerate(s):
        if i > 0 and table[c] > table[s[i-1]]:
            ans = ans - table[s[i-1]] + (table[c] - table[s[i-1]])
        else:
            ans += table[c]

    return ans


print(romanToInt("III"), 3)
print(romanToInt("IV"), 4)
print(romanToInt("IX"), 9)
print(romanToInt("LVIII"), 58)
print(romanToInt("MCMXCIV"), 1994)
