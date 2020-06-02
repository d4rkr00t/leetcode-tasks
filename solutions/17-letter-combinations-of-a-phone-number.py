# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(4^n) n number of inputs, then we map to 4 possible values
# Space: O(4^n)
#
# Solution:
# TBD

def letterCombinations(digits: str) -> [str]:
    digits = [int(i) - 1 for i in list(digits)]
    num_to_letters = [
        [],
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]
    ]

    def gen(prev, letters):
        if not prev:
            return letters

        next = []
        for l in letters:
            for p in prev:
                next.append(p + l)

        return next

    prev = []
    for d in digits:
        letters = num_to_letters[d]
        prev = gen(prev, letters)

    return prev

print(letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


