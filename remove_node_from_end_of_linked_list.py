'''
Brute Force Method
First pass: count the total number of nodes. Second pass: traverse to the 
(length - n)th node and remove the next node.

Time Complexity: O(n) (two passes through the list)

Space Complexity: O(1) (only pointer variables)
def removeNthFromEnd(head, n):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    if n == length:
        return head.next
    
    curr = head
    for i in range(length - n - 1):
        curr = curr.next
    curr.next = curr.next.next
    return head

'''

'''
Optimal Method (Two Pointers - One Pass)
Use two pointers with n+1 gap between them. When the right pointer reaches the end, 
the left pointer will be at the node before the one to be removed. Use a dummy node 
to handle edge cases.

Time Complexity: O(n) (single pass through the list)

Space Complexity: O(1) (only pointer variables)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #add dummy node with value 0 before the start so value is zero and next ptr is head
        dummy=ListNode(0,head)
        left=dummy
        right=head

        #we set left to dummy and right to head+n(in next step)
        # so when right reaches end, we will be at n-1 where we can change pointer
        while n>0:
            right=right.next
            n-=1
        #^ correct way to set right to head +n

        while right:
            left=left.next
            right=right.next
        #now left is at n-1
        #by doing the below operation we delete a value and set ptr to its necct value    
        left.next=left.next.next
        return dummy.next

        