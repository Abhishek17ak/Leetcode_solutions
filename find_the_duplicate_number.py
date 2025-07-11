'''
Brute Force Method
Check every pair of elements to find the duplicate, or use a hash set to track seen elements.

Time Complexity: O(n²) for nested loops, or O(n) with hash set

Space Complexity: O(1) for nested loops, or O(n) with hash set
def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

'''
'''
Optimal Method (Floyd's Cycle Detection - Tortoise and Hare)
Treat the array as a linked list where nums[i] points to index nums[i]. Since there's a duplicate, there must be a cycle. Use Floyd's algorithm to find the cycle, then find the entrance to the cycle (which is the duplicate number).

Time Complexity: O(n) (two phases of cycle detection)

Space Complexity: O(1) (only two pointer variables)
'''
def findDuplicate(nums):
    slow, fast = 0, 0
    
    # Phase 1: Find intersection point in the cycle
    while True:
        slow = nums[slow]           # Move 1 step
        fast = nums[nums[fast]]     # Move 2 steps
        if slow == fast:            # Cycle detected
            break
    
    # Phase 2: Find entrance to the cycle (duplicate number)
    slow2 = 0                       # Start second pointer at beginning
    while True:
        slow = nums[slow]           # Move both pointers 1 step
        slow2 = nums[slow2]
        if slow == slow2:           # Found entrance (duplicate)
            return slow

        