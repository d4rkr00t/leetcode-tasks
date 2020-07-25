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
    state = 0
    cache = {}
    ff = False

    for n in cells:
        state = (state << 1) | n

    while N:
        if not ff:
            if state in cache:
                N %= cache[state] - N
                ff = True
            else:
                cache[state] = N

        if N > 0:
            N -= 1
            state = ~(state << 1) ^ (state >> 1)
            state &= 0x7e

    res = []
    for i in range(len(cells)):
        res.append(state & 0x1)
        state >>= 1

    return res[::-1]


print(prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7), [
      0, 0, 1, 1, 0, 0, 0, 0])
print(prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000), [
      0, 0, 1, 1, 1, 1, 1, 0])
