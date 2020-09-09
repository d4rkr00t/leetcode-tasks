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

    def is_valid(index, last):
        if used[index]:
            return False

        if last == -1:
            return True

        if (index + last) % 2 == 1:
            return True

        mid = (index+last) // 2

        if mid == 4:
            return used[mid]

        if index % 3 != last % 3 and index//3 != last//3:
            return True

        return used[mid]

    def calc(last, size):
        if size == 0:
            return 1

        sum = 0
        for i in range(9):
            if is_valid(i, last):
                used[i] = True
                sum += calc(i, size - 1)
                used[i] = False

        return sum

    for i in range(m, n+1):
        ans += calc(-1, i)
        used = [False] * 9

    return ans


print(numberOfPatterns(m=1, n=1), 9)
