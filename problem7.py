# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


## so to begin with, we understand that palindrome word has to be read same forward and backward.
## note that any uppercase letters are converted into lower case letters
## note that this could include numbers as well
## we need to check if the word is palindrome and return output of true/false

## How am i going to solve this solution?
### First thought was to use the split, and reverse method
### Then checking for if the string is equal to the reverse string, then return true


def isPalindrome(s: str):
    check = s.reverse()
    print(check)

isPalindrome('racecar')

#found out there is no 'reverse' method in python
#you can still use the slice method
