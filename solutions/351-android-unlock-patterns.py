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
    ans = 0
    used = [False] * 9

    def is_valid(idx, last):
        if used[idx]:
            return False

        if last == -1:
            return True

        if (idx + last) % 2 == 1:
            return True

        mid = (idx + last) // 2
        if mid == 4:
            return used[mid]

        if idx % 3 != last % 3 and idx//3 != last // 3:
            return True

        return used[mid]

    def calc_patterns(last, i):
        nonlocal ans, used

        if i == 0:
            return 1

        s = 0

        for j in range(9):
            if is_valid(j, last):
                used[j] = True
                s += calc_patterns(j, i-1)
                used[j] = False

        return s

    for i in range(m, n+1):
        ans += calc_patterns(-1, i)
        used = [False] * 9

    return ans


print(numberOfPatterns(m=1, n=1), 9)
print(numberOfPatterns(m=1, n=3), 385)
