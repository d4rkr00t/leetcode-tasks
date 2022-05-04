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
    nums = [1, 6, 8, 9]
    table = {1: 1, 6: 9, 8: 8, 9: 6, 0: 0}
    ans = 0

    def backtrack(cur, rotation, digit):
        nonlocal ans

        if cur != rotation:
            ans += 1

        for num in nums + [0]:
            tmp = cur * 10 + num
            if tmp <= n:
                backtrack(tmp, table[num] * digit + rotation, digit * 10)

    for num in nums:
        backtrack(num, table[num], 10)

    return ans


print(confusingNumberII(20), 6)
print(confusingNumberII(100), 19)

# [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
