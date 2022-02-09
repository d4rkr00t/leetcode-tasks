# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/
# medium
#
# Tags: Google, Microsoft, Amazon, Facebook
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Stack

from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
        if a > 0:
            stack.append(a)
            continue

        while stack and stack[-1] > 0 and a < 0:
            prev = stack.pop()

            if prev == abs(a):
                a = None
                break
            elif prev > abs(a):
                a = prev

        if a:
            stack.append(a)

    return stack


# input = [5, 10, -5]
# stack = [5, 10]
# a     = 10
# prev  = 10

print(asteroidCollision([5, 10, -5]), [5, 10])
print(asteroidCollision([8, -8]), [])
print(asteroidCollision([10, 2, -5]), [10])
print(asteroidCollision([-2, 2, -3]), [-2, -3])
