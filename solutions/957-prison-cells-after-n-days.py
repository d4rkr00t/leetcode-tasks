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

from typing import List


def prisonAfterNDays(cells: List[int], N: int) -> List[int]:
    state = 0
    for c in cells:
        state = (state << 1) | c

    def next_day():
        return ~((state >> 1) ^ (state << 1)) & 0x7e

    seen = {}
    skipped_duplicate = False

    while N:
        if state in seen and not skipped_duplicate:
            N = N % (seen[state] - N)
            skipped_duplicate = True
        else:
            seen[state] = N

        if N > 0:
            N -= 1
            state = next_day()

    ans = [0] * 8
    i = 0

    while state:
        state, q = divmod(state, 2)
        ans[i] = q
        i += 1

    ans.reverse()

    return ans


print(prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7), [
      0, 0, 1, 1, 0, 0, 0, 0])
print(prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000), [
      0, 0, 1, 1, 1, 1, 1, 0])

# 01011001
#
# 00101100
# 10110010
#
# 01100000
