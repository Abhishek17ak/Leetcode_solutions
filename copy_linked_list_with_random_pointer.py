'''Brute Force Method
For each node in the original list, create a new node. Then for each new node, find the corresponding random node by traversing the original list to find its index, then traverse the new list to that index.

Time Complexity: O(n²) (for each node, may need to traverse the entire list to find random pointer)

Space Complexity: O(n) (for the new list)

def copyRandomList(head):
    if not head:
        return None
    
    nodes = []
    curr = head
    while curr:
        nodes.append(Node(curr.val))
        curr = curr.next
    
    curr = head
    for i in range(len(nodes)):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if curr.random:
            j = 0
            temp = head
            while temp != curr.random:
                temp = temp.next
                j += 1
            nodes[i].random = nodes[j]
        curr = curr.next
    
    return nodes[0] if nodes else None

'''
'''
Optimal Method (Hash Map - Two Pass)
Use a hash map to store the mapping from original nodes to copied nodes. First pass: create all new nodes and store the mapping. Second pass: set next and random pointers using the hash map.

Time Complexity: O(n) (two passes through the list)

Space Complexity: O(n) (hash map and new list)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            oldToCopy[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        return oldToCopy[head]
        