# 1281. Subtract the Product and Sum of Digits of an Integer

# Given an integer number n, 
# return the difference between the product of its digits
# and the sum of its digits.

# Examples
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21

def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n != 0:
            last = n % 10 #this goes through the n from last number to first number
            sum += last
            product *= last
            n = n//10
        return product - sum

# Leetcode accepts the problem!

# How can i implement this with for loop though?
def subtractProductAndSum(self, n: int) -> int:
        new=str(n)              # makes the number into string
        nlist=list(new)         # makes the string into list.
        newlist=[]              # create an empty bracklet to push the nlist
        for i in nlist:             # loop around the nlist to push each row into newList
            newlist.append(int(i))  # append pushes the number into bracket
        mul=1
        sum=0
        for i in range(len(newlist)):
            mul=mul*newlist[i]
            sum+=newlist[i]
        dif=mul-sum
        return (dif)

# need to turn the 3 digit number into a LIST. (Line 36-40)