# 1480. Running Sum of 1d Array

## Given an array nums. We define a running sum of an array 
# as runningSum[i] = sum(nums[0]…nums[i])
# Return the running sum of nums.

# Example
## Input: nums = [1,2,3,4]
## Output: [1,3,6,10]
## Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

## Input: nums = [1,1,1,1,1]
## Output: [1,2,3,4,5]
## Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

## Input: nums = [3,1,2,10,1]
## Output: [3,4,6,16,17]

# How to solve the problem:
# Since there is an array, we just return the sum everytime we go through the for loop

def sumOfOneArray(nums):
    sum = 0
    array = []
    for i in range(len(nums)):
        sum += nums[i]
        array += [sum]
    return array

# Leetcode accepted the problem solving!

## Big o notation is
# Time complexity of O(n) where n equals length of nums
# Space complexity of O(w) where w equals to longest sum in nums