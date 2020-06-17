# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1)

def romanToInt(s: str) -> int:
    table = {
        "": 0,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    i = ans = 0

    while i < len(s):
        if i == len(s) - 1:
            ans += table[s[i]]
            break

        if table[s[i+1]] > table[s[i]]:
            ans += table[s[i+1]] - table[s[i]]
            i += 2
        else:
            ans += table[s[i]]
            i += 1

    return ans


print(romanToInt("III"), 3)
print(romanToInt("IV"), 4)
print(romanToInt("IX"), 9)
print(romanToInt("LVIII"), 58)
print(romanToInt("MCMXCIV"), 1994)
