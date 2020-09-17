# Candy
# https://leetcode.com/problems/candy/
# hard
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


from typing import List


def candy(ratings: List[int]) -> int:
    candies = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(len(candies)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)


print(candy([1, 0, 2]), 5)
print(candy([1, 2, 2]), 4)
