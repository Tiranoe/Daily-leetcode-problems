# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Given Example
#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.

#Input: s = "   fly me   to   the moon  "
#Output: 4
#Explanation: The last word is "moon" with length 4.

#Input: s = "luffy is still joyboy"
#Output: 6
#Explanation: The last word is "joyboy" with length 6.


## step by step thought process
## I got stuck? Why?
## I couldn't figure out if something is a word
## A word is a list of consecutive letters without spaces 


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        length = 0
        for i in range(len(s)):
        ## iterate through string s
            char = s[i]
            if char == " ":
                if len(word) > 0:
                    length = len(word)
                    #print(word, length)
                word = ""
            else:
                word += char
        if len(word) > 0:
            length = len(word)
        #print(length)
        return length
    
