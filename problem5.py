
# this function puts out the string into split elements in an array
#first = [*s]
#second = [*t]
# print(first)


##for i in [*s]:
##    for j in [*t]:
##        if i == j:
##            i.pop()
##            j.pop()
##    if not s:
##        print('true')

# this answer does not work because str object has no attribute of 'pop' function
def validAnagram(s,t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    # figured out that this part of the solution is solved with method called HASHMAP
    # very useful!

validAnagram('anagram', 'naagarm')

#Putting my thought process i put on leetcode here
    # we intially start with two string variables: s and t.
    # Put these split function into an empty array
    # We should need to split the string into each letters
    # Iterate first letter of first string into the second string, and take them out if they match
    # when the array becomes empty, we can confirm that t is an anagram of s.
    # Output will be returned as true, otherwise, returned as false
        
        
    ## Question to ask: Is there a simpler way to iterate this through sorting by alphabet letters in the array? Maybe a built in function for python?
    #### thought of the fact that since anagram has to use up all letters to check, we can check for the length of the string and return false if it doesn't match up
