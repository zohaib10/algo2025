# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


def productsOfArrayExceptSelf(nums) -> List[int]:

    res = [0] * len(nums)
    #prefix
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre = pre * nums[i]
    
    post = 1
    for j in range(len(nums) - 1, -1, -1):
        temp = res[j]
        res[j] = temp * post
        post = nums[j] * post
        
    return res


# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
print(productsOfArrayExceptSelf([1,2,3,4]))

#prefix: [1, 1, 2, 6]
#final: [24,12,8,6]