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
        "9": ["w", "x", "y", "z"],
    }

    ans = [""]

    for d in digits:
        next_ans = []
        for ch in table[d]:
            for comb in ans:
                next_ans.append(comb + ch)

        ans = next_ans

    return ans


print(letterCombinations("23"),
      ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
