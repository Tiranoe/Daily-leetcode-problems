# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

## Examples
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

#Input: head = [1,2]
#Output: [2,1]

#Input: head = []
#Output: []

## pseudocode
### in order to solve this problem, since this is in an array, we need to split everything, 
### reverse the order, and then join them back together

#def reversedList(head):
    #head.reverse()
    #print(head)

#reversedList([1,2,3,4,5])
# solution works! with one simple reverse command - i guess python doesn't need to split

def reversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while(head):
        nex = head.next
        head.next = prev
        prev = head
        head = nex
    return prev

reversedList([1,2,3,4,5])
#this solution is solved using the nodes Linked List