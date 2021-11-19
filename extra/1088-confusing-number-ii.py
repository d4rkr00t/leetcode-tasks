# Confusing Number II
# https://leetcode.com/problems/confusing-number-ii/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def confusingNumberII(n: int) -> int:
    nums = [1, 6, 8, 9, 0]
    table = {1: 1, 6: 9, 8: 8, 9: 6, 0: 0}
    found = set()
    ans = 0

    def backtrack(cur, rotation, digit):
        nonlocal ans, n

        if cur > n:
            return

        if rotation != cur and cur not in found:
            ans += 1
            found.add(cur)

        for num in nums:
            next = cur * 10 + num
            backtrack(next, table[num] * digit + rotation, digit * 10)

    for num in nums:
        if num != 0:
            backtrack(num, table[num], 10)

    return ans


# {98, 68, 6, 9, 10, 16, 81, 18, 19, 80, 86, 89, 90, 91, 60, 61}
# [66,68,80,81,86,89,90,91,98,99,100].
print(confusingNumberII(20), 6)
print(confusingNumberII(100), 19)

# n = 20
# 9 1 6
# 0
# 0
# 8
#
