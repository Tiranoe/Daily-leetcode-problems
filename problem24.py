# 392. Is Subsequence

## Given two strings s and t, 
## return true if s is a subsequence of t, or false otherwise.
## A subsequence of a string is a new string 
## that is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## Examples
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false

# we need to iterate through t string first every s value. (so use maybe two for loop method)
# Another way I could think of is using hashmap.
# but unsure how i would do so.

def isSubsqn(s, t):
    sl, tl = 0, 0
        
    while sl<len(s) and tl<len(t):
        if s[sl] == t[tl]:
            sl+=1
        tl+=1
    return sl==len(s)