# Group Anagrams - Medium level

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## How to solve the problem

# call an empty object for the hashmap
from collections import defaultdict

def Solution(strs):
    diction = defaultdict(list)
    result = []
    for i in range(len(strs)):
        letters = sorted([*strs[i]]) # makes the sorted split word [a, e, t]
        #print(letters)
        if diction[tuple(letters)]:
            diction[tuple(letters)].append(strs[i])
        #print(diction)
        else:
            diction[tuple(letters)] = [strs[i]]
    # print(diction) -> shows all the answers we need
    return list(diction.values())


    #for i in range(len(strs)):
        #diction.append(strs[i])
        #print(diction)
    #for e, str in enumerate(strs):
        #print(e, str)
        #for e, str in enumerate(strs):
            #print(e, str)
        # for char, string in enumerate(str):
            # print(char, string)


Solution(["eat","tea","tan","ate","nat","bat"])