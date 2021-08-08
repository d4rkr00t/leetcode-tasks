# Find the Longest Valid Obstacle Course at Each Position
#
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def longestObstacleCourseAtEachPosition(obstacles: List[int]) -> List[int]:
    ans = [0] * len(obstacles)
    ans[0] = 1
    table = {}
    table[obstacles[0]] = 1

    for i in range(1, len(obstacles)):
        cur = obstacles[i]
        prev = obstacles[i - 1]

        if cur >= prev:
            j = i - 1
        else:
            j = i - 1
            while cur < obstacles[j] and j >= 0:
                j -= 1

        if j < 0:
            ans[i] = 1
        else:
            ans[i] = max(ans[j] + 1, table.get(cur, 0) + 1)

        table[cur] = ans[i]

    return ans


print(longestObstacleCourseAtEachPosition(obstacles=[1, 2, 3, 2]),
      [1, 2, 3, 3])
print(longestObstacleCourseAtEachPosition(obstacles=[2, 2, 1]), [1, 2, 1])
print(longestObstacleCourseAtEachPosition(obstacles=[3, 1, 5, 6, 4, 2]),
      [1, 1, 2, 3, 2, 2])

print(
    longestObstacleCourseAtEachPosition(
        obstacles=[5, 1, 5, 5, 1, 3, 4, 5, 1, 4]),
    [1, 1, 2, 3, 2, 3, 4, 5, 3, 5])

# [1, 2, 3, 4, 2, 1, 2]
#  1  2  3  4  1  1  2
