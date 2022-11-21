# I want to focus back to hashing and hashmap

## Given an integer array nums, return true if any value 
# appears at least twice in the array, 
# and return false if every element is distinct.

## I am going to solve this problem by using hashmap by introducting an empty object first

def DuplicateNumbers(nums):
    countNums = {}
    for i in range(len(nums)):
        countNums[nums[i]] = 1 + countNums(nums[i], 0)
        if countNums[nums[i]] == 2:
            return True

nums = [1,2,3,1]
DuplicateNumbers(nums)

#solutions works in leetcode