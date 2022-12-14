# 724. Find Pivot Index

## Given an array of integers nums, calculate the pivot index of this array.
## The pivot index is the index where the sum of all the numbers strictly 
## to the left of the index is equal to the sum of all the numbers strictly 
## to the index's right.
## If the index is on the left edge of the array, then the left sum is 0 
## because there are no elements to the left. This also applies to the right edge 
## of the array.
## Return the leftmost pivot index. If no such index exists, return -1.

## Examples
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

        #leftSum = 0
        #rightSum = 0
        #for i in range(len(nums)):
        #    leftSum += nums[i]
        #    #print(leftSum) => this displays all sum for every iteration
        #for j in reversed(len(nums)):
        #    print(nums[j])

        ## this solution is not going to work, need to find a different way to solve the problem

# Maybe we can use from total addition of all the sums to approach this
# thinking of using the total minus the index in every iteration to get the rightsum

def solution(nums):
    total= sum(nums)
    temp = 0
    for i in range(len(nums)):
        if(nums[i] == total - 2*temp): 
            return i
        temp += nums[i]
    return -1

#this solution works! Leetcode accepted