# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

## Examples
# () => True
# [](){} => True
# (] => False

## Pseudocode -
### First thought is for the code to detect a opening parenthesis, bracket, block
### Then we need to ensure that code checks for closing side right after the first one

## I had the question of if it needs to close it right away - but problem description tells us that it needs to closed in correct order
## Maybe we can use the for loop to go through the string s 

def validParenthesis(s):
    stack = []
    hash = {"(":")", "{":"}", "[":"]"}
    
    for char in s:
        if char not in hash:
            stack.append(char)
            continue
        if not stack or stack[-1] != hash[char]:
            return False
        stack.pop()

    return not stack

# solution works!
