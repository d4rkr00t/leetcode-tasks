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
    ans = [1] * len(ratings)

    for i in range(1,len(ratings)):
        curr = ratings[i]
        prevr = ratings[i-1]
        if curr > prevr:
            ans[i] = max(ans[i-1] + 1, ans[i])

    for i in range(len(ratings)-2,-1,-1):
        curr = ratings[i]
        prevr = ratings[i+1]
        if curr > prevr:
            ans[i] = max(ans[i+1] + 1, ans[i])

    return sum(ans)


print(candy([1, 0, 2]), 5)
print(candy([1, 2, 2]), 4)
