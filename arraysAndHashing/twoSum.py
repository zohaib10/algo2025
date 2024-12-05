# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twoSum(nums, target):

    myDict = {}
    for i in range(len(nums)):
        n = nums[i]
        x = target - n
        if x in myDict:
            return [myDict[x], i]
        myDict[n] = i


# Example 1 -> Input: nums = [2,7,11,15], target = 9
# Output: [0,1] -> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
print(twoSum([2,7,11,15], 9))

# Example 2 -> Input: nums = [3,2,4], target = 6 -> Output: [1,2]
print(twoSum([3,2,4], 6))

# Example 3 -> Input: nums = [3,3], target = 6 -> Output: [0,1]
print(twoSum([3,3], 6))