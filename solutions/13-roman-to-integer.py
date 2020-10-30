# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1)

def romanToInt(s: str) -> int:
    table = {"": 0, "I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    prev = ""
    for ch in s:
        ans += table[ch]
        if table[ch] > table[prev]:
            ans -= table[prev] * 2

        prev = ch

    return ans


print(romanToInt("III"), 3)
print(romanToInt("IV"), 4)
print(romanToInt("IX"), 9)
print(romanToInt("LVIII"), 58)
print(romanToInt("MCMXCIV"), 1994)
