'''
Brute Force Method
Store all node values in an array, then create a new linked list with values in reverse order.

Time Complexity: O(n) (traverse twice: once to collect values, once to create new list)

Space Complexity: O(n) (for storing values in array)
def reverseList(head):
    if not head:
        return None
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    values.reverse()
    new_head = ListNode(values[0])
    curr = new_head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return new_head

'''
'''
Optimal Method (Iterative Pointer Reversal)
Use three pointers (prev, curr, temp) to reverse the links in-place. 
For each node, save the next node, reverse the current node's pointer to point 
to the previous node, then move all pointers forward.

Time Complexity: O(n) (single pass through the list)

Space Complexity: O(1) (only using a few pointer variables)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr= None, head

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev    

        