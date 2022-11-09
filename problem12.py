# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

## Examples
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

## Pseudocode
# in the given array, we need to iterate for each element in the given ascending array to locate the target number
# when it find the location, we need to return the index of the target in the given array
# if not, we return -1
# NOTE that this needs to be algorithm with 0(log n) runtime complexity which means that we need to divide and conquer
## this means that we need a left and right point and middle point to compare and throw away one side of the array since it's ascending order

def binarySearch(nums, target):
    left = 0
    right = len(nums - 1)

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
        
# when finding the middle number = right+left/2 can lead to overflow(?) since it could be infinite.
# correct way is middle = left + ((right - left) // 2)

## solution accepted