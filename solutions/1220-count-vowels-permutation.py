# Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/
# hard
#
# Tags: Atlassian, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def countVowelPermutation(n: int) -> int:
    table = {
        "a": ["e", "i", "u"],
        "e": ["a", "i"],
        "i": ["e", "o"],
        "o": ["i"],
        "u": ["o", "i"],
    }

    dp = {
        "a": [0] * (n),
        "e": [0] * (n),
        "i": [0] * (n),
        "o": [0] * (n),
        "u": [0] * (n),
    }

    MOD = 10**9 + 7

    for ch in table.keys():
        dp[ch][0] = 1

    for i in range(1, n):
        for ch in table.keys():
            dp[ch][i] = sum([dp[c][i - 1] for c in table[ch]]) % MOD

    return sum([dp[c][-1] for c in table.keys()]) % MOD


print(countVowelPermutation(1), 5)
print(countVowelPermutation(2), 10)
print(countVowelPermutation(3), 19)
print(countVowelPermutation(4), 35)
print(countVowelPermutation(5), 68)

#   1  2  3  4 5
# a 1  3  6
# e 1  2  5
# i 1  2  3
# o 1  1  2
# u 1  2  3
#   5 10 19
# a = 2 + 1

# table = {
#         "a": ["e", "i", "o"],
#         "e": ["a", "i"],
#         "i": ["e", "o"],
#         "o": ["i"],
#         "u": ["o", "i"],
#     }
