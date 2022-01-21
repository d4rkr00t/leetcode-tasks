# Optimal Account Balancing
# https://leetcode.com/problems/optimal-account-balancing/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minTransfers(transactions: List[List[int]]) -> int:
    people = [0] * 20
    ans = float("inf")

    def applyTransaction(f, t, amount):
        people[f] -= amount
        people[t] += amount

    for f, t, v in transactions:
        applyTransaction(f, t, v)

    negatives = [abs(n) for n in people if n < 0]
    positives = [n for n in people if n > 0]

    def backtrack(idx, tr):
        nonlocal ans
        if idx >= len(negatives):
            ans = min(ans, tr)
            return

        neg = negatives[idx]

        for j, pos in enumerate(positives):
            if pos == 0: continue

            diff = pos - neg
            if diff >= 0:
                positives[j] = diff
                backtrack(idx + 1, tr + 1)
            else:
                positives[j] = 0
                negatives[idx] = neg - pos
                backtrack(idx, tr + 1)

            positives[j] = pos
            negatives[idx] = neg

    backtrack(0, 0)

    return ans


print(minTransfers([[0, 1, 10], [2, 0, 5]]), 2)
print(minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]), 1)
print(minTransfers([[0, 1, 5], [0, 2, 3], [0, 3, 2]]), 3)

# [0,0,0]
# 0->1 +10
# [-10,10,0]
# 2->0 +5
# [-5,10,-5]
#
# [0,0,0]
# 0 -> 1 +10
# [-10,10,0]
# 1 -> 0 +1
# [-9,9,0]
# 1 -> 2 +5
# [-9,4,5]
# 2 -> 0 +5
# [-4,4,0]

# [-10, 5, 3, 2]
