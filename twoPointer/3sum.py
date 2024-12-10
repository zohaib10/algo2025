# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List
def threeSum(nums: List[int], ) -> List[List[int]]:
    
    res = []
    nums.sort()
    for i, num in enumerate(nums):
        #go next if the current num is the same as previous
        if i != 0 and nums[i - 1] == num:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            if num + nums[l] + nums[r] > 0:
                r -= 1
            elif num + nums[l] + nums[r] < 0:
                l += 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return res


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
print(threeSum([-1,0,1,2,-1,-4]))

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
print(threeSum([0,1,1]))

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
print(threeSum([0,0,0]))