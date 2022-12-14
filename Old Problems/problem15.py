# Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list 
# that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

## Examples
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

#Input: head = [1,2], pos = 0
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

#Input: head = [1], pos = -1
#Output: false
#Explanation: There is no cycle in the linked list.

# Unsure how I would solve this with Linked List.. let's think about it
# we need to use the comparison method with slow and fast
# if fast ever catches up, it will equal to slow cycle, then the problem will betrue

def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == next:
            return True
    return False

# easy to understand if you think in a diagram
# the Big O Notation is O(n) - constant time

#leet code won't accept the solution due to time issue..? trying again next time