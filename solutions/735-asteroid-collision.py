# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/
# medium
#
# Tags: Google, Microsoft, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    def canCollide(a, b):
        return a >= 0 and b < 0

    for a in asteroids:
        if not stack:
            stack.append(a)
            continue

        cur = a
        while stack and canCollide(stack[-1], cur):
            prev = stack.pop()
            if abs(prev) > abs(cur):
                cur = prev
            elif abs(prev) < abs(cur):
                pass
            else:
                cur = None
                break

        if cur != None:
            stack.append(cur)

    return stack


print(asteroidCollision([5, 10, -5]), [5, 10])
print(asteroidCollision([8, -8]), [])
print(asteroidCollision([10, 2, -5]), [10])
