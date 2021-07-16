# Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
# hard
#
# Tags: DP
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def colorTheGrid(self, m: int, n: int) -> int:
    def getColor(mask, pos):
        return (mask >> (2 * pos)) & 3

    def setColor(mask, pos, color):
        return mask | (color << (2 * pos))

    def dfs(r, curColMask, prevColMask, out):
        if r == m:
            out.append(curColMask)
            return

        for i in [1, 2, 3]:
            if getColor(prevColMask, r) != i and (
                    r == 0 or getColor(curColMask, r - 1) != i):
                dfs(r + 1, setColor(curColMask, r, i), prevColMask, out)

    @lru_cache(None)
    def nei(prevColMask):
        out = []
        dfs(0, 0, prevColMask, out)
        return out

    @lru_cache(None)
    def dp(c, prevColMask):
        if c == n: return 1
        ans = 0
        for ne in nei(prevColMask):
            ans = (ans + dp(c + 1, ne)) % 1_000_000_007
        return ans

    return dp(0, 0)


# r g b r
# g r g
#
