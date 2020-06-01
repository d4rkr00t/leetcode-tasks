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
    def bt(i, j, used, count):
        nonlocal m, n, ans

        count += 1
        if count > n: return

        used.add((i,j))

        if count <= n and count >= m:
            ans += 1

        for di, dj in [(-1,-1), (-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (-1, -1), (0, -1)]:
            x = i + di
            y = j + dj

            if not (x, y) in used and x >= 0 and x < 3 and y >= 0 and y < 3:
                bt(x, y, used, count)

        used.remove((i,j))

    for i in range(3):
        for j in range(3):
            bt(i, j, set(), 0)

    return ans


print(numberOfPatterns(m = 1, n = 1), 9)
print(numberOfPatterns(m = 1, n = 2), 65)
