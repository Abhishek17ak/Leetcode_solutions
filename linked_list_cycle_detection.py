'''
Brute Force Method
Use a hash set to track visited nodes. For each node, check if it's already in the set. 
If yes, a cycle exists; if no, add it to the set and continue.

Time Complexity: O(n) (visit each node once)

Space Complexity: O(n) (hash set to store visited nodes)
def hasCycle(head):
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False

'''
'''
Optimal Method (Floyd's Cycle Detection Algorithm - Tortoise and Hare)
Use two pointers: slow (moves 1 step) and fast (moves 2 steps). 
If there's a cycle, the fast pointer will eventually catch up to the slow pointer 
inside the loop.

Time Complexity: O(n) (each node visited at most twice)

Space Complexity: O(1) (only two pointer variables)
'''

def hasCycle(head):
    slow, fast = head, head         # Initialize both pointers to head
    
    while fast and fast.next:       # Ensure fast can move 2 steps
        slow = slow.next            # Move slow pointer 1 step
        fast = fast.next.next       # Move fast pointer 2 steps
        if slow == fast:            # Pointers meet - cycle detected
            return True
    return False                    # Fast reached end - no cycle
     
        