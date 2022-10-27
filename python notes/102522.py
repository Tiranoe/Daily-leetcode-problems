## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through the array of integers in nums
        # For each iteration, iterate through the array from the next index to the end of array
        # Within this nested loop, add the element from the outer loop to the element in the inner loop
        # If the sum of the elements is equal to target integer, find the index of the elements in the array
        # Return the indices of the two elements
        

O(n*n) - quadratic run time
O(n) - Linear run time
O(1) - Constant Time [Fastest]

hashing,hashmap