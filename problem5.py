
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
    s = 'anagram'
    t = 'naagarm'
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