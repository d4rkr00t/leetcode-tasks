# Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# medium
#
# Tags:
#
# Time:  O(n)
# Space: O(n)

from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:
    table = {0: -1}
    s = ans = 0

    for i, n in enumerate(nums):
        s += n
        key = s - k

        if key in table:
            ans = max(ans, i - table[key])

        table.setdefault(s, i)

    return ans


print(maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3), 4)
print(maxSubArrayLen(nums=[-2, -1, 2, 1], k=1), 2)
print(maxSubArrayLen(nums=[1], k=0), 0)
print(maxSubArrayLen(nums=[1, 1, 0], k=1), 2)
