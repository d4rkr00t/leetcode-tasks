# Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/
# medium
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def prisonAfterNDays(cells: [int], N: int) -> [int]:
    def toNum(cells):
        num = 0
        for n in cells:
            num = (num << 1) | n
        return num

    def toArr(num, numCells):
        arr = [0] * numCells
        cur = 0
        while cur < numCells:
            arr[cur] = 1 if num & 1 else 0
            num = num >> 1
            cur += 1

        arr.reverse()
        return arr

    def nextDay(num):
        res = ~((num << 1) ^ (num >> 1)) & 0x7e
        return res

    numCells = 8
    num = toNum(cells)
    seen = {}
    looped = False

    while n:
        if num in seen and not looped:
            n = n % (seen[num] - n)
            looped = True
        else:
            seen[num] = n

        if n > 0:
            n -= 1
            num = nextDay(num)

    return toArr(num, numCells)


print(prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7),
      [0, 0, 1, 1, 0, 0, 0, 0])

print(prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000),
      [0, 0, 1, 1, 1, 1, 1, 0])

# 0 1 0 1 1 0 0 1
# 1 0 1 1 0 0 1 0
# 0 0 1 0 1 1 0 0
# 0 1 1 0 0 0 0 0
