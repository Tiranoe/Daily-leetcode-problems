## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.


# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Let's think through each step in solving this.
        # Iterate through the array of integers in nums
        # For each iteration, iterate through the array from the next index to the end of array
        # Within this nested loop, add the element from the outer loop to the element in the inner loop
        # If the sum of the elements is equal to target integer, find the index of the elements in the array
        # Return the indices of the two elements
        


import random
import time

def two_sum(nums, target):
    # O(N^2) where N is length of nums
    # O(1) space
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_optimized(nums, target):
    # O(N) time, O(N) space
    # hashset = { <nums[index]>: <index> } 
    hashset = { n: i for i, n in enumerate(nums) }
    for i in range(len(nums)):
        n = nums[i]
        complement = target - n
        if complement in hashset and hashset[complement] != i:
            return [hashset[complement], i]

print("Building Test Case...")
nums = []
count = 90000 # <---- You can play around with this number and see how it changes the outcome 
for i in range(count):
    n = random.randint(2, 100)
    nums.append(n)
nums.append(1)
nums.append(0)
target = 1

print("Starting Solutions...")

start = time.time()
print("Optimized Solution: ", two_sum_optimized(nums, target), f"{round(time.time()-start, 3)}seconds")
start = time.time()
print("Brute Force Solution: ", two_sum(nums, target), f"{round(time.time()-start, 3)}seconds")
print("Done!")


## The Concept of Big O Notation

#O(n*n) - quadratic run time
#O(n) - Linear run time
#O(1) - Constant Time [Fastest]

# So what is hashing and hashmap, and importance of them?


