# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# HashTable

def subarraySum(nums: [int], k: int) -> int:
    count = s = 0
    dict = { 0: 1 }

    for i,n in enumerate(nums):
        s += n
        if s-k in dict:
            count += dict[s-k]

        dict[s] = dict.get(s, 0) + 1

    return count

print(subarraySum(nums = [1,1,1], k = 2), 2)

