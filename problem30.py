# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Examples
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# step by step thoughts
# so the first thing I thought of was to just iterate through the List nums to find the index
# First example would bypass that with the method
# second example would need to include if nums[i] is greater than target, you return i
# third example would just return i, if it finish iterating but didn't not find anything

def searchInsert(self, nums: int, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    if nums != 0:
        return len(nums)

#leetcode accepts the answer