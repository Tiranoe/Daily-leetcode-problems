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
            