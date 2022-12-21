# switching to python language after talking with my coding mentor
# Using neetcode.io to continue on with my daily update of solving data/algo

#   This is the problem
## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def two_sum_optimized(nums, target):
    # keep in mind that hashset = { <nums[index]>: <index> }
    hashset = { n: i for i, n in enumerate(nums)}
    for i in range(len(nums)):
        n = nums[i]
        complement = target - n
        if complement in hashset and hashset[complement] != i:
            return [hashset[complement], i]