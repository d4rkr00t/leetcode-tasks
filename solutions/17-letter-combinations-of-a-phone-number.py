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

def letterCombinations(digits: str) -> [str]:
    if not digits:
        return []

    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    ans = mapping[digits[0]]

    for d in digits[1:]:
        next = []
        for m in mapping[d]:
            for a in ans:
                next.append(a + m)

        ans = next

    return ans


print(letterCombinations("23"), ["ad", "ae",
                                 "af", "bd", "be", "bf", "cd", "ce", "cf"])
