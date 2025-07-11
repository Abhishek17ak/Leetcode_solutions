'''
Brute Force Method
Repeatedly scan the string and remove any adjacent matching pairs of brackets ("()", "[]", "{}") until no more can be removed. If the string is empty at the end, it's valid.

Time Complexity: O(n²) (since each scan can remove only one pair, and there can be up to n/2 scans)

Space Complexity: O(n) (for the intermediate string)

def isValid(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""

'''
'''
Optimal Method (Stack)
Use a stack to track opening brackets. For each closing bracket, 
check if the top of the stack is the matching opening bracket. 
If so, pop it; otherwise, return False. At the end, the stack should be empty.

Time Complexity: O(n) (each character is pushed/popped at most once)

Space Complexity: O(n) (stack can grow up to n/2 in the worst case)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                                      # Stack to track opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }  # Map closing to opening brackets
        
        for c in s:                                     # Check each character
            if c in closeToOpen:                        # If it's a closing bracket
                if stack and stack[-1] == closeToOpen[c]:  # Check if it matches
                    stack.pop()                         # Remove matching opening bracket
                else:
                    return False                        # No match found - invalid
            else:                                       # If it's an opening bracket
                stack.append(c)                         # Add to stack
                
        return True if not stack else False             # Valid if stack is empty
