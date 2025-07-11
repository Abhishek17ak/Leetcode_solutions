'''
Brute Force Method
Maintain a normal stack. For getMin, scan the entire stack to find the minimum value.

Time Complexity:
push: O(1)
pop: O(1)
top: O(1)
getMin: O(n) (linear scan for min)

Space Complexity: O(n) (for the stack)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

'''
'''
Optimal Method (Two Stacks)
Use two stacks: one for all values, another to track the current minimum at each level.
On push, push the new value and the new min; on pop, pop both stacks.

Time Complexity: O(1) for all operations (push, pop, top, getMin)

Space Complexity: O(n) (for both stacks)
'''

class MinStack:
    def __init__(self):
        self.stack = []         # Main stack for actual values
        self.minStack = []      # Helper stack to track minimums

    def push(self, val: int) -> None:
        self.stack.append(val)  # Add value to main stack
        # Add current minimum to minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()        # Remove from main stack
        self.minStack.pop()     # Remove from min stack

    def top(self) -> int:
        return self.stack[-1]   # Return top of main stack

    def getMin(self) -> int:
        return self.minStack[-1]  # Return top of min stack (current minimum)
