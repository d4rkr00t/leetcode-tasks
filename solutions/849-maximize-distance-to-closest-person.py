# Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# easy
#
# Tags: Amazon, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution: Two Pointers

def maxDistToClosest(seats: [int]) -> int:
    people = (i for i,seat in enumerate(seats) if seat)
    prev, future = None, next(people)
    ans = 0
    inf = float("inf")

    for i, seat in enumerate(seats):
        future = future if future is None or i < future else next(people, None)
        if seat:
            prev = i
        else:
            left = inf if prev is None else i - prev
            right = inf if future is None else future - i

            ans = max(ans, min(left, right))

    return ans


print(maxDistToClosest([1,0,0,0,1,0,1]), 2)
print(maxDistToClosest([1,0,0,0]), 3)
print(maxDistToClosest([0,0,0,1]), 3)
