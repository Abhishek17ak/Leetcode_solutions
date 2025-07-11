'''
Brute Force Method
Store all nodes in an array, then reorder by creating new connections between nodes at positions [0, n-1, 1, n-2, 2, n-3, ...].

Time Complexity: O(n) (traverse once to collect, once to reorder)

Space Complexity: O(n) (array to store all nodes)
def reorderList(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    
    l, r = 0, len(nodes) - 1
    while l < r:
        nodes[l].next = nodes[r]
        l += 1
        if l < r:
            nodes[r].next = nodes[l]
            r -= 1
    nodes[l].next = None

'''
'''
Optimal Method (Find Middle + Reverse + Merge)
Three-step approach:

Find middle using slow/fast pointers

Reverse second half of the list

Merge first half and reversed second half alternately

Time Complexity: O(n) (three linear passes)

Space Complexity: O(1) (only pointer variables)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast= head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            #now fast is at end and slow is at middle
        
        #now we will reverse the second half
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        #done

        #now merge two 
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
            
        