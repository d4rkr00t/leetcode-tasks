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
    state_mask = 0
    seen = {}
    isFastFoward = False

    for n in cells:
        state_mask <<= 1
        state_mask = (state_mask | n)

    while N > 0:
        if not isFastFoward:
            if state_mask in seen:
                N %= seen[state_mask] - N
                isFastFoward = True
            else:
                seen[state_mask] = N

        if N > 0:
            N -= 1
            state_mask = ~((state_mask << 1) ^ (state_mask >> 1))
            state_mask = state_mask & 0x7e


    res = [0] * len(cells)
    for i in range(len(cells))[::-1]:
        res[i] = (state_mask & 1)
        state_mask = state_mask >> 1

    return res


print(prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], N = 7), [0,0,1,1,0,0,0,0])
print(prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], N = 1000000000), [0,0,1,1,1,1,1,0])
