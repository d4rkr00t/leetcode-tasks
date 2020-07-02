# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# easy
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def maxDistToClosest(seats: [int]) -> int:
    left = [0] * len(seats)
    right = [0] * len(seats)
    N = len(seats) - 1

    for i in range(N+1):
        if seats[i] == 0:
            if i == 0: left[i] = float("inf")
            else: left[i] = 1 if seats[i-1] == 1 else left[i-1] + 1

        if seats[N - i] == 0:
            j = N - i
            if j == N: right[j] = float("inf")
            else: right[j] = 1 if seats[j+1] == 1 else right[j+1] + 1

    dist = 0

    for i in range(N+1):
        dist = max(dist, min(left[i], right[i]))

    return dist

print(maxDistToClosest([1,0,0,0,1,0,1]), 2)
print(maxDistToClosest([1,0,0,0]), 3)
print(maxDistToClosest([0,0,0,1]), 3)
