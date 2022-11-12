#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. 
#The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

## Examples
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]

#Input: list1 = [], list2 = []
#Output: []

#Input: list1 = [], list2 = [0]
#Output: [0]

## How are you going to solve the problem?
## First, my first initial way to solve the problem was to add each list in an empty array
## When it gets added, it iterates through the array and places itself when it's less than the number
## Use the for loop to iterate through the whole array as it adds each number
## Problem wants to solve it with linked nodes but unsure how to solve that.
