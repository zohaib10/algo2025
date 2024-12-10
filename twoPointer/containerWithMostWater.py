# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from typing import List

def maxArea(height: List[int]):
    maxArea = 0
    l = 0
    r = len(height) - 1

    while l < r:
        left = height[l]
        right = height[r]
        area = (r - l) * min(left, right)
        maxArea = max(area, maxArea)
        if left < right:
            l += 1
        else:
            r -= 1
    return maxArea


# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
print(maxArea([1,8,6,2,5,4,8,3,7]))

# Example 2:
# Input: height = [1,1]
# Output: 1
print(maxArea([1,1]))