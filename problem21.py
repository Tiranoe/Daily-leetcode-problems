# Longest Common Prefix

# Write a function to find the longest common prefix string 
# amongst an array of strings.
# If there is no common prefix, return an empty string "".

## Example
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Understading the problem
# I believe we need to use the method of len(strs) to grab each length of each word in the array
# And then use the If statement to grab the longest common prefix in the array
# then return the longest common prefix or empty string if none exists
# probably need to use hashmapping

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" #returns empty string if there are no common prefix
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest): # this already created the hashmap
            #print(i, char)
            for other in strs: #this calls up the list of words in the array
                #print(other)
                if other[i] != char: #comparing each letter of each word to the shortest word
                    return shortest[:i]
        return shortest # returns the fl into the output