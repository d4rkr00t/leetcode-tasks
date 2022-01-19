# Android Unlock Patterns
# https://leetcode.com/problems/android-unlock-patterns/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def numberOfPatterns(m: int, n: int) -> int:
    count = 0

    def can_add(pattern, num):
        if not pattern:
            return True

        cur = pattern[-1]

        if (num + cur) % 2 == 1:
            return True

        mid = (num + cur) // 2

        if mid == 4:
            return mid in pattern

        if num % 3 != cur % 3 and num // 3 != cur // 3:
            return True

        return mid in pattern

    def bactrack(pattern):
        nonlocal count

        if len(pattern) > n:
            return

        if m <= len(pattern) <= n:
            count += 1

        for i in range(9):
            if i not in pattern:
                if can_add(pattern, i):
                    pattern.append(i)
                    bactrack(pattern)
                    pattern.pop()

    bactrack([])

    return count


# 1 2 3
# 4 5 6
# 7 8 9

print(numberOfPatterns(m=1, n=1), 9)
print(numberOfPatterns(m=1, n=2), 65)
print(numberOfPatterns(m=1, n=3), 385)
