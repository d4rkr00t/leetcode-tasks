# Tiling a Rectangle with the Fewest Squares
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def tilingRectangle(n: int, m: int) -> int:
    best = m * n

    def dfs(height, moves):
        nonlocal best
        if all(h == n for h in height):
            best = min(best, moves)
            return

        if moves >= best:
            return

        min_height = min(height)
        idx = height.index(min_height)
        ridx = idx + 1
        while ridx < m and height[ridx] == min_height:
            ridx += 1

        for i in range(min(ridx - idx, n - min_height), 0, -1):
            new_height = height[:]

            for j in range(i):
                new_height[idx + j] += i

            dfs(new_height, moves + 1)

    dfs([0] * m, 0)
    return best


print(tilingRectangle(n=2, m=3), 3)
print(tilingRectangle(n=5, m=8), 5)
print(tilingRectangle(n=11, m=13), 6)

# - - - - - - - -
#
#
#
#
#
