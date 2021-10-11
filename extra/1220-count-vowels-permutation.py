# Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def countVowelPermutation(n: int) -> int:
    letters = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    prev = {
        "a": ["e", "u", "i"],
        "e": ["a", "i"],
        "i": ["o", "e"],
        "o": ["i"],
        "u": ["i", "o"]
    }
    dp = [[0] * 6 for _ in range(n + 1)]

    for i in range(5):
        dp[1][i + 1] = 1

    for i in range(2, n + 1):
        for ch, j in letters.items():
            for p in prev[ch]:
                dp[i][j + 1] += dp[i - 1][letters[p] + 1]

    return sum(dp[-1]) % (10**9 + 7)


print(countVowelPermutation(1), 5)
print(countVowelPermutation(2), 10)
print(countVowelPermutation(5), 68)

#   0 1 2
#   0 0 0
# a 0 1 3
# e 0 1 2
# i 0 1 2
# o 0 1 1
# u 0 1 2
