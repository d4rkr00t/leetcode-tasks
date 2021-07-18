# Maximum Genetic Difference Query
# https://leetcode.com/contest/weekly-contest-250/problems/maximum-genetic-difference-query/
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


def maxGeneticDifference(parents: List[int],
                         queries: List[List[int]]) -> List[int]:
    def find(i, val):
        cur = val ^ i
        if parents[i] != -1:
            return max(cur, find(parents[i], val))

        return cur

    ans = []

    for i, v in queries:
        ans.append(find(i, v))

    return ans


print(
    maxGeneticDifference(parents=[-1, 0, 1, 1],
                         queries=[[0, 2], [3, 2], [2, 5]]), [2, 3, 7])

print(
    maxGeneticDifference(parents=[3, 7, -1, 2, 0, 7, 0, 2],
                         queries=[[4, 6], [1, 15], [0, 5]]), [6, 14, 7])
