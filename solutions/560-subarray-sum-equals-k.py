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
    ans = sum = 0
    table = {0: 1}

    for n in nums:
        sum += n
        if sum - k in table:
            ans += table[sum - k]

        table[sum] = table.get(sum, 0) + 1

    return ans


print(subarraySum(nums=[1, 1, 1], k=2), 2)
