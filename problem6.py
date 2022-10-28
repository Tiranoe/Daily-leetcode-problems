# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

## Given examples
#Input: nums = [1,2,3,1]
#Output: true

#Input: nums = [1,2,3,4]
#Output: false

#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true

## My example would be:
#Input: nums = [1,2,3,3]
#Output: true

## Pseudocoding what the step by step thought processes
## First initial thought would be to use the hashmapping to solve this equation
# In the given array of integers, we need to hashmap through it to check each value
# iterate through the array
# If hashmap has more than one value, then output comes as false
# If not, will come out as true

def containsDuplicate(nums):
    nums = [1,2,3,4]
    countNums = {}

    for i in range(len(nums)):
        countNums[nums[i]] = 1 + countNums.get(nums[i], 0)
        if countNums[nums[i]] == 2:
            return False