'''
Brute Force Method
Convert both linked lists to integers, add them, then convert the result back 
to a linked list in reverse order.

Time Complexity: O(max(m, n)) where m and n are lengths of the lists

Space Complexity: O(max(m, n)) for the result list 
(but may have integer overflow issues for very large numbers)
'''
'''
Optimal Method (Digit-by-Digit Addition with Carry)
Simulate elementary school addition: add corresponding digits from both lists along with any carry from the previous addition. Handle different list lengths and final carry.

Time Complexity: O(max(m, n)) where m and n are lengths of the lists

Space Complexity: O(max(m, n)) for the result list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummy node before head
        dummy=ListNode()
        cur=dummy
        carry=0

        while l1 or l2 or carry:
            #set values
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            #calcualtions
            val=v1+v2+carry
            carry=val//10 #a // 10 removes the last digit.
            val=val%10 #a % 10 gives you the last digit.
            cur.next=ListNode(val)     

            #set pointers
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
