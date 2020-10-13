# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# medium
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:
    if not T:
        return None

    ans = [0] * len(T)
    stack = []

    for i in range(len(T))[::-1]:
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i

        stack.append(i)

    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [
      1, 1, 4, 2, 1, 1, 0, 0])

# 76
# 0 0 1 1 2 4 1 1
