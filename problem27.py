# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Examples
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, 
# we return the second one.

## We can easily find the middle node of the linked list by dividing the total by 2
## If it's a fraction, we will round it down (or take out the decimal)

# can't do above method, since we are using linked list

def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# leetcode accepted solution