'''
Brute Force Method
Store all values from both linked lists in an array, sort the array, 
then create a new linked list from the sorted values.

Time Complexity: O(n log n) (due to sorting, where n is total number of nodes)

Space Complexity: O(n) (for storing values in array)

def mergeTwoLists(list1, list2):
    values = []
    curr = list1
    while curr:
        values.append(curr.val)
        curr = curr.next
    curr = list2
    while curr:
        values.append(curr.val)
        curr = curr.next
    values.sort()
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return head

'''
'''
Optimal Method (Two Pointers Merge)
Use a dummy node and two pointers to merge the lists in-place. 
Compare values at current positions of both lists, attach the smaller node to the result, 
and advance that pointer.

Time Complexity: O(n + m) (where n and m are lengths of the two lists)

Space Complexity: O(1) (only using a few pointer variables)
'''

def mergeTwoLists(list1, list2):
    dummy = node = ListNode()           # Dummy node to simplify logic

    while list1 and list2:              # While both lists have nodes
        if list1.val < list2.val:       # Compare values
            node.next = list1           # Attach smaller node
            list1 = list1.next          # Move pointer forward
        else:
            node.next = list2           # Attach smaller node
            list2 = list2.next          # Move pointer forward
        node = node.next                # Move result pointer forward

    if list1:                           # Attach remaining nodes
        node.next = list1
    else:
        node.next = list2

    return dummy.next                   # Return head (skip dummy)
