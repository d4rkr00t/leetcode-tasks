# Maximum Compatibility Score Sum
# https://leetcode.com/contest/weekly-contest-251/problems/maximum-compatibility-score-sum/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxCompatibilitySum(students: List[List[int]],
                        mentors: List[List[int]]) -> int:
    def toInt(arr):
        i = 0
        for n in arr:
            i = (i << 1) | n

        return i

    def count(num, n):
        res = 0
        for i in range(n):
            if num & 1:
                res += 1

            num = num >> 1

        return res

    n = len(students[0])
    students = [toInt(s) for s in students]
    mentors = [toInt(s) for s in mentors]
    grid = [[0] * len(students) for _ in range(len(students))]
    ans = 0

    for i, s in enumerate(students):
        for j, m in enumerate(mentors):
            grid[j][i] = count(~(m ^ s), n)

    def backtrack(col, row, used, sum):
        if row == len(grid):
            return sum

        sum += grid[row][col]
        used.add(col)
        tmp = 0

        for i in range(len(grid[0])):
            if i in used:
                continue
            tmp = max(tmp, backtrack(i, row + 1, used, 0))

        used.remove(col)
        return tmp + sum

    for i in range(len(grid[0])):
        ans = max(ans, backtrack(i, 0, set(), 0))

    return ans


print(
    maxCompatibilitySum(students=[[1, 1, 0], [1, 0, 1], [0, 0, 1]],
                        mentors=[[1, 0, 0], [0, 0, 1], [1, 1, 0]]), 8)
print(
    maxCompatibilitySum(students=[[0, 0], [0, 0], [0, 0]],
                        mentors=[[1, 1], [1, 1], [1, 1]]), 0)

print(
    maxCompatibilitySum(students=[[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1],
                                  [1, 0, 1, 1, 0, 0]],
                        mentors=[[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1],
                                 [0, 1, 0, 0, 1, 1]]), 10)

print(
    maxCompatibilitySum(students=[[0, 0, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0],
                                  [0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1],
                                  [1, 0, 1, 1, 1, 1, 1]],
                        mentors=[[0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1],
                                 [0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1],
                                 [1, 1, 1, 1, 1, 0, 0]]), 24)

print(
    maxCompatibilitySum(students=[[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]],
                        mentors=[[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0]]),
    9)

# [[1,1,1],[0,0,1],[0,0,1],[0,1,0]]
# [[1,0,1],[0,1,1],[0,1,0],[1,1,0]]
