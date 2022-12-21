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


# def isPalindrome(s: str):
  #   together = s.replace(" ", "").replace(",", "").replace(':!@#$%^&*();.', '').lower()
    # check = together[::-1]
    # print(check)
    # print(together)
    # if check == together:
    #     print('True')
    # if check != together:
    #     return False

# isPalindrome('A man, a plan, a canal: Panama')

#found out there is no 'reverse' method in python
#you can still use the slice method

## [::-1] slice method works

## Need to find a way to remove spaces - replace method => replace(' ', "")
## Need to find a method for speical characters to be gone??
## apparently there is a method called: isalnum() => which gets rid of all special char

def isPalindrome(s: str):
    joined = ''.join(e for e in s if e.isalnum()).lower()
    reversed = joined[::-1]
    if joined == reversed:
        return True

isPalindrome('A man, a plan, a canal: Panama')

# CODE WORKS YES

##Given solution is something different
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

 # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )