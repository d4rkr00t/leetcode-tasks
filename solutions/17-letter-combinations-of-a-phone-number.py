# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(4^n)
# Space: O(4^n)
#
# Solution:
# TBD

from typing import List


def letterCombinations(digits: str) -> List[str]:
    table = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    ans = []

    def backtrack(pos, cur):
        if pos >= len(digits):
            ans.append("".join(cur))
            return

        digit = digits[pos]
        for letter in table[digit]:
            cur.append(letter)
            backtrack(pos + 1, cur)
            cur.pop()

    backtrack(0, [])

    return ans


print(letterCombinations("23"),
      ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
