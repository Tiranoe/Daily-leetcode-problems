# Best Time to buy and sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Example (1)
# Input: prices = [7,1,5,3,6,4]
# Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

## Example (2)
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


## Pseudocode
### In an array of prices where it iterates on indices and for each indices it results the prices of a given stock. (i stands for each day)
### The point is to maximize profit by subtracting the price on 2nd day (of highest stock price) with the price on 1st day (the lowest day [hopefully?])
### If there is a case of not gaining any profit at all, we return 0.
### Also mindful that we need to buy FIRST then sell.

### How are you going to solve the problem?
#### I think since the given prices are an iterated array, we need to go through comparison and get the lowest number possible before subsituting.
#### If there is no highest number than the first number in array, then we return 0
#### After we get to find the lowest and highest integer in the array, we subtract those number to get the output. 

def Solution(prices):
    lowest = prices[0]
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
            # this gets the lowest number
        elif prices[i] - lowest > maxProfit:
            maxProfit = prices[i] - lowest
            # this finds the biggest and maxProfit at the same time
    return(maxProfit)

Solution([7,1,5,3,6,4])

# Solution works in leetcode