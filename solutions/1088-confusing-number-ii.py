# Confusing Number II
# https://leetcode.com/problems/confusing-number-ii/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def confusingNumberII(n: int) -> int:
    table = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
    ans = 0

    def backtrack(num, rotated, unit):
        nonlocal ans
        if num > n:
            return

        if num != rotated:
            ans += 1

        for d, dr in table:
            if d == 0 and num == 0: continue
            backtrack(num * 10 + d, dr * unit + rotated, unit * 10)

    backtrack(0, 0, 1)

    return ans


print(confusingNumberII(20), 6)
print(confusingNumberII(100), 19)
