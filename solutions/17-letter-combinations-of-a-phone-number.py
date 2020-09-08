# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from turtle import back
from typing import List


def letterCombinations(digits: str) -> List[str]:
    dl_map = {
        "0": [],
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    ans = []

    def backtrack(cur, pos):
        if pos == len(digits):
            if cur:
                ans.append("".join(cur))
            return

        for c in dl_map[digits[pos]]:
            cur.append(c)
            backtrack(cur, pos + 1)
            cur.pop()

    backtrack([], 0)

    return ans


print(letterCombinations("23"), ["ad", "ae",
                                 "af", "bd", "be", "bf", "cd", "ce", "cf"])
