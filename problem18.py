# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes
# along the longest path from the root node down to the farthest leaf node.

## Examples
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Input: root = [1,null,2]
# Output: 2

## How are you going to solve this code?
# First, We need to think about using binary tree method to solve this solution
# since we have the class of Tree (self, left, right)
# first indicated if root is empty, then we return 0
# second, we either decide to solve this recursive, iterative, or BFS(?)

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(self, root) -> int:
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Leetcode accepted problem