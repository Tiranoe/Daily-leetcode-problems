# Invert Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.

## Example
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Input: root = [2,1,3]
# Output: [2,3,1]

# Input: root = []
# Output: []

## How am I going to solve this question?
## First thing about the tree problem is that every time you go down a row:
## The number of the numbers are multipled by 2 (1 -> 2 -> 4 -> 8, etc)
## We can even find a mathematical way to check the root of binary tree with these numbers
## maybe a for loop using the multipled by 2, method mentioned above?

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None # this is for checking if root has numbers
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
